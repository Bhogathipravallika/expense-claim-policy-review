from django.shortcuts import render, redirect

from .forms import ExpenseClaimForm
from .policy import validate_claim
from .ai_classifier import classify_expense
from .utils import calculate_total_claims
from .policy_evidence import get_policy_evidence


def create_claim(request):

    if request.method == 'POST':

        form = ExpenseClaimForm(request.POST)

        if form.is_valid():

            claim = form.save(commit=False)

            # AI classification
            ai_category, ai_confidence = classify_expense(
                claim.description
            )

            claim.ai_category = ai_category
            claim.ai_confidence = ai_confidence

            # Policy validation
            errors = validate_claim(
                claim.claimant,
                claim.date,
                claim.category,
                claim.amount,
                claim.receipt_available
            )

            # Policy evidence
            policy_evidence = get_policy_evidence(
                claim.category
            )

            # Policy errors
            if errors:

                claim.status = "Review Required"

                claim.review_message = (
                    "This claim requires review because: "
                    + " ".join(errors)
                )

                return render(
                    request,
                    'claims/create_claim.html',
                    {
                        'form': form,
                        'policy_errors': errors,
                        'policy_evidence': policy_evidence,
                        'review_message': claim.review_message,
                    }
                )

            # AI confidence check
            if ai_confidence == "Low":

                claim.status = "Review Required"

                claim.review_message = (
                    "AI classification has low confidence. "
                    "Reviewer verification is required."
                )

            else:

                claim.status = "Pending"

                claim.review_message = (
                    "Claim passed the initial policy checks "
                    "and is pending reviewer approval."
                )

            claim.save()

            return redirect('claim_success')

        else:

            return render(
                request,
                'claims/create_claim.html',
                {
                    'form': form,
                    'missing_information': True,
                }
            )

    else:

        form = ExpenseClaimForm()

    return render(
        request,
        'claims/create_claim.html',
        {
            'form': form
        }
    )


def claim_success(request):

    total = calculate_total_claims()

    return render(
        request,
        'claims/success.html',
        {
            'total': total
        }
    )