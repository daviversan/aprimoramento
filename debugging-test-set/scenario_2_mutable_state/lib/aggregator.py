def group_by_category(records, groups={}):
    """Group a list of transaction records by their 'category' field.

    Each record is a dict like {"category": "travel", "amount": 150}.
    Returns a dict mapping category -> list of amounts.

    Example:
        records = [
            {"category": "travel", "amount": 100},
            {"category": "food",   "amount": 50},
            {"category": "travel", "amount": 200},
        ]
        group_by_category(records)
        # => {"travel": [100, 200], "food": [50]}
    """
    # BUG: mutable default argument — `groups` persists across calls
    for record in records:
        cat = record["category"]
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(record["amount"])
    return groups


def compute_totals(records):
    """Return a dict mapping category -> total amount.

    Example:
        records = [
            {"category": "travel", "amount": 100},
            {"category": "food",   "amount": 50},
            {"category": "travel", "amount": 200},
        ]
        compute_totals(records)
        # => {"travel": 300, "food": 50}
    """
    grouped = group_by_category(records)
    totals = {}
    for category, amounts in grouped.items():
        totals[category] = sum(amounts)
    return totals


def top_categories(records, n):
    """Return the top `n` categories by total spend, as a list of
    (category, total) tuples sorted descending by total.

    Example:
        top_categories(records, 1)  # => [("travel", 300)]
    """
    totals = compute_totals(records)
    sorted_cats = sorted(totals.items(), key=lambda x: x[1], reverse=True)

    # BUG: should return first n items but uses n as exclusive end with
    # an off-by-one — returns n-1 items when n >= 1
    return sorted_cats[: n - 1] if n > 0 else []
