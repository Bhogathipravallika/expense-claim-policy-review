POLICY_EVIDENCE = {
    "Travel": {
        "limit": 5000,
        "evidence": "Travel expenses are allowed up to ₹5,000 per claim. A receipt is required."
    },
    "Food": {
        "limit": 1000,
        "evidence": "Food expenses are allowed up to ₹1,000 per claim. A receipt is required."
    },
    "Accommodation": {
        "limit": 5000,
        "evidence": "Accommodation expenses are allowed up to ₹5,000 per claim. A receipt is required."
    },
    "Office": {
        "limit": 2000,
        "evidence": "Office expenses are allowed up to ₹2,000 per claim. A receipt is required."
    },
    "Other": {
        "limit": 1000,
        "evidence": "Other expenses are allowed up to ₹1,000 per claim. A receipt is required."
    },
}


def get_policy_evidence(category):
    policy = POLICY_EVIDENCE.get(category)

    if policy:
        return policy["evidence"]

    return "No specific policy evidence available."