def calculate_fee(amount, fee_rate):
    """Calculate fee on a transaction.

    The fee is a percentage of the transaction amount.
    For example, calculate_fee(1000, 0.025) should return 25.0
    (2.5% of 1000).
    """
    return amount * fee_rate


def calculate_total_with_tax(amount, fee_rate, tax_rate):
    """Calculate the total charge for a transaction including fee and tax.

    The tax is applied to the fee, NOT to the original amount.
    Total = amount + fee + tax_on_fee

    Example:
        amount = 1000, fee_rate = 0.02, tax_rate = 0.10
        fee = 1000 * 0.02 = 20
        tax_on_fee = 20 * 0.10 = 2
        total = 1000 + 20 + 2 = 1022
    """
    fee = calculate_fee(amount, fee_rate)
    # BUG: tax is applied to the original amount instead of to the fee
    tax = amount * tax_rate
    return amount + fee + tax


def split_expense(total, num_people):
    """Split an expense equally among `num_people`.

    Returns the per-person amount rounded to 2 decimal places.
    """
    if num_people <= 0:
        raise ValueError("Number of people must be at least 1")

    # BUG: integer division (//) truncates to int, losing decimal precision
    per_person = total // num_people
    return round(per_person, 2)
