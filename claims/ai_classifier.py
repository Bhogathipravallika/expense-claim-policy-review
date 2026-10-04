def classify_expense(description):
    description = description.lower()

    if any(word in description for word in [
        "uber", "taxi", "bus", "train", "flight", "travel", "fuel"
    ]):
        return "Travel", "High"

    if any(word in description for word in [
        "lunch", "dinner", "breakfast", "food", "restaurant", "meal"
    ]):
        return "Food", "High"

    if any(word in description for word in [
        "hotel", "room", "stay", "accommodation"
    ]):
        return "Accommodation", "High"

    if any(word in description for word in [
        "stationery", "office", "printer", "paper", "supplies"
    ]):
        return "Office", "High"

    return "Other", "Low"