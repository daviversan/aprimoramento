import os
import sys
from datetime import date

_scenario_dir = os.path.join(os.path.dirname(__file__), "..")
for _key in list(sys.modules.keys()):
    if _key == "lib" or _key.startswith("lib."):
        del sys.modules[_key]
if _scenario_dir not in sys.path:
    sys.path.insert(0, _scenario_dir)

from lib.spend_report import (
    EXPENSES,
    filter_by_date_range,
    employee_totals,
    category_summary,
    flag_over_budget,
)


# ---------- filter_by_date_range ----------

def test_filter_full_range():
    """Filtering from Jan 1 to Mar 31 should return all 7 expenses."""
    result = filter_by_date_range(EXPENSES, date(2025, 1, 1), date(2025, 3, 31))
    assert len(result) == 7


def test_filter_single_month():
    """January 2025 has 2 expenses (Alice travel, Bob software)."""
    result = filter_by_date_range(EXPENSES, date(2025, 1, 1), date(2025, 1, 31))
    assert len(result) == 2


def test_filter_boundary_inclusive():
    """An expense on exactly end_date should be included."""
    result = filter_by_date_range(EXPENSES, date(2025, 3, 20), date(2025, 3, 20))
    assert len(result) == 1
    assert result[0]["employee"] == "Alice"
    assert result[0]["amount"] == 950


def test_filter_empty_range():
    result = filter_by_date_range(EXPENSES, date(2024, 1, 1), date(2024, 12, 31))
    assert result == []


# ---------- employee_totals ----------

def test_employee_totals_all():
    totals = employee_totals(EXPENSES)
    assert totals == {"Alice": 2235, "Bob": 800, "Carol": 195}


def test_employee_totals_filtered():
    jan = filter_by_date_range(EXPENSES, date(2025, 1, 1), date(2025, 1, 31))
    totals = employee_totals(jan)
    assert totals == {"Alice": 1200, "Bob": 500}


# ---------- category_summary ----------

def test_category_summary_counts():
    """Should count number of transactions, NOT sum amounts."""
    summary = category_summary(EXPENSES)
    assert summary == {"travel": 3, "meals": 2, "software": 2}


def test_category_summary_filtered():
    jan = filter_by_date_range(EXPENSES, date(2025, 1, 1), date(2025, 1, 31))
    summary = category_summary(jan)
    assert summary == {"travel": 1, "software": 1}


# ---------- flag_over_budget ----------

def test_flag_over_budget_500():
    flagged = flag_over_budget(EXPENSES, 500)
    assert len(flagged) == 2
    assert flagged[0]["amount"] == 1200
    assert flagged[1]["amount"] == 950


def test_flag_over_budget_100():
    flagged = flag_over_budget(EXPENSES, 100)
    assert len(flagged) == 5
    amounts = [f["amount"] for f in flagged]
    assert amounts == [1200, 950, 500, 300, 150]


def test_flag_over_budget_none_flagged():
    flagged = flag_over_budget(EXPENSES, 5000)
    assert flagged == []
