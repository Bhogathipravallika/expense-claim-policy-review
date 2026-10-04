from .models import ExpenseClaim
from datetime import date as today_date


POLICY_LIMITS = {
    "Travel": 5000,
    "Food": 1000,
    "Accommodation": 5000,
    "Office": 2000,
    "Other": 1000,
}


def validate_claim(claimant, date, category, amount, receipt_available):
    errors = []

    # Future date check
    if date > today_date.today():
        errors.append("Claim date cannot be in the future.")

    # Category limit
    limit = POLICY_LIMITS.get(category)

    if limit and amount > limit:
        errors.append(
            f"Amount exceeds {category} policy limit of ₹{limit}."
        )

    # Receipt check
    if not receipt_available:
        errors.append("Receipt is required.")

    # Duplicate check
    duplicate = ExpenseClaim.objects.filter(
        claimant=claimant,
        date=date,
        category=category,
        amount=amount
    ).exists()

    if duplicate:
        errors.append("Duplicate claim detected.")

    return errors