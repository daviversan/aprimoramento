import os
import sys

_scenario_dir = os.path.join(os.path.dirname(__file__), "..")
for _key in list(sys.modules.keys()):
    if _key == "lib" or _key.startswith("lib."):
        del sys.modules[_key]
if _scenario_dir not in sys.path:
    sys.path.insert(0, _scenario_dir)

from lib.calculator import calculate_fee, calculate_total_with_tax, split_expense


# ---------- calculate_fee ----------

def test_fee_basic():
    assert calculate_fee(1000, 0.025) == 25.0


def test_fee_zero_rate():
    assert calculate_fee(500, 0) == 0


# ---------- calculate_total_with_tax ----------

def test_total_with_tax():
    """amount=1000, fee_rate=0.02, tax_rate=0.10
    fee = 20, tax_on_fee = 2, total = 1022
    """
    result = calculate_total_with_tax(1000, 0.02, 0.10)
    assert result == 1022.0


def test_total_with_tax_no_fee():
    result = calculate_total_with_tax(500, 0, 0.10)
    assert result == 500.0


def test_total_with_tax_no_tax():
    result = calculate_total_with_tax(500, 0.05, 0)
    assert result == 525.0


# ---------- split_expense ----------

def test_split_expense_even():
    assert split_expense(100, 4) == 25.0


def test_split_expense_uneven():
    assert split_expense(100, 3) == 33.33


def test_split_expense_one_person():
    assert split_expense(77.50, 1) == 77.50


def test_split_expense_rejects_zero_people():
    try:
        split_expense(100, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
