from .models import ExpenseClaim


def calculate_total_claims():
    total = 0

    claims = ExpenseClaim.objects.all()

    for claim in claims:
        total += claim.amount

    return total