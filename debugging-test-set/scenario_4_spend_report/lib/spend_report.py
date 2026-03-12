from datetime import date


EXPENSES = [
    {"employee": "Alice", "category": "travel",    "amount": 1200, "date": date(2025, 1, 15)},
    {"employee": "Alice", "category": "meals",     "amount": 85,   "date": date(2025, 2, 3)},
    {"employee": "Bob",   "category": "software",  "amount": 500,  "date": date(2025, 1, 20)},
    {"employee": "Bob",   "category": "travel",    "amount": 300,  "date": date(2025, 3, 10)},
    {"employee": "Carol", "category": "meals",     "amount": 45,   "date": date(2025, 2, 28)},
    {"employee": "Carol", "category": "software",  "amount": 150,  "date": date(2025, 3, 15)},
    {"employee": "Alice", "category": "travel",    "amount": 950,  "date": date(2025, 3, 20)},
]


def filter_by_date_range(expenses, start_date, end_date):
    """Return expenses whose date is within [start_date, end_date] inclusive.

    Both boundaries should be included.
    """
    result = []
    for exp in expenses:
        # BUG: uses strict inequality on end_date — excludes expenses on end_date
        if exp["date"] >= start_date and exp["date"] < end_date:
            result.append(exp)
    return result


def employee_totals(expenses):
    """Return a dict mapping employee name -> total amount spent."""
    totals = {}
    for exp in expenses:
        name = exp["employee"]
        if name not in totals:
            totals[name] = 0
        totals[name] += exp["amount"]
    return totals


def category_summary(expenses):
    """Return a dict mapping category -> number of transactions in that category."""
    summary = {}
    for exp in expenses:
        cat = exp["category"]
        if cat not in summary:
            summary[cat] = 0
        # BUG: adds the amount instead of counting the transaction (should be += 1)
        summary[cat] += exp["amount"]
    return summary


def flag_over_budget(expenses, budget):
    """Return a list of expenses whose amount is strictly greater than `budget`.

    The returned list should be sorted by amount descending (highest first).
    """
    flagged = []
    for exp in expenses:
        if exp["amount"] > budget:
            flagged.append(exp)

    # BUG: sorts ascending instead of descending (missing reverse=True)
    flagged.sort(key=lambda x: x["amount"])
    return flagged
