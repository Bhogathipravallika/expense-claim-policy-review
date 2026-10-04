from django.contrib import admin
from .models import ExpenseClaim


@admin.register(ExpenseClaim)
class ExpenseClaimAdmin(admin.ModelAdmin):

    list_display = (
        'claimant',
        'date',
        'category',
        'amount',
        'currency',
        'receipt_available',
        'ai_category',
        'ai_confidence',
        'status',
        'reviewer_decision',
        'reviewer_category',
        'reviewer_reason',
        'review_message',
    )

    actions = [
        'approve_claim',
        'reject_claim',
        'request_clarification',
        'override_category',
    ]

    @admin.action(description='Approve selected claims')
    def approve_claim(self, request, queryset):
        queryset.update(
            status='Approved',
            reviewer_decision='Approved',
            reviewer_reason='Approved by reviewer',
            review_message='Claim approved by reviewer.'
        )

    @admin.action(description='Reject selected claims')
    def reject_claim(self, request, queryset):
        queryset.update(
            status='Rejected',
            reviewer_decision='Rejected',
            reviewer_reason='Rejected by reviewer',
            review_message='Claim rejected by reviewer.'
        )

    @admin.action(description='Request clarification')
    def request_clarification(self, request, queryset):
        queryset.update(
            status='Clarification Required',
            reviewer_decision='Clarification',
            reviewer_reason='More information required',
            review_message='More information is required before a final decision.'
        )

    @admin.action(description='Override AI classification')
    def override_category(self, request, queryset):
        queryset.update(
            reviewer_decision='Override',
            reviewer_reason='AI classification overridden by reviewer',
            status='Review Required',
            review_message='AI classification overridden by reviewer.'
        )