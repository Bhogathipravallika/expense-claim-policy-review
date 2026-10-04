from django.db import models


class ExpenseClaim(models.Model):

    CATEGORY_CHOICES = [
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Accommodation', 'Accommodation'),
        ('Office', 'Office'),
        ('Other', 'Other'),
    ]

    claimant = models.CharField(max_length=100)

    date = models.DateField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10,
        default='INR'
    )

    description = models.TextField()

    receipt_available = models.BooleanField(
        default=False
    )

    # AI classification
    ai_category = models.CharField(
        max_length=50,
        blank=True
    )

    ai_confidence = models.CharField(
        max_length=20,
        blank=True
    )

    # Claim status
    status = models.CharField(
        max_length=30,
        default='Pending'
    )

    # Reviewer decision
    reviewer_decision = models.CharField(
        max_length=30,
        blank=True
    )

    # Reviewer category override
    reviewer_category = models.CharField(
        max_length=50,
        blank=True
    )

    # Reviewer reason
    reviewer_reason = models.TextField(
        blank=True
    )

    # Explanation of review outcome
    review_message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.claimant} - {self.amount}"