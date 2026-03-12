import os
import sys

_scenario_dir = os.path.join(os.path.dirname(__file__), "..")
for _key in list(sys.modules.keys()):
    if _key == "lib" or _key.startswith("lib."):
        del sys.modules[_key]
if _scenario_dir not in sys.path:
    sys.path.insert(0, _scenario_dir)

from lib.aggregator import group_by_category, compute_totals, top_categories


RECORDS_A = [
    {"category": "travel", "amount": 100},
    {"category": "food", "amount": 50},
    {"category": "travel", "amount": 200},
]

RECORDS_B = [
    {"category": "software", "amount": 400},
    {"category": "software", "amount": 100},
]


# ---------- group_by_category ----------

def test_group_by_category_basic():
    result = group_by_category(RECORDS_A)
    assert result == {"travel": [100, 200], "food": [50]}


def test_group_by_category_independent_calls():
    """Two separate calls with different datasets should NOT leak state."""
    result_a = group_by_category(RECORDS_A)
    result_b = group_by_category(RECORDS_B)
    assert result_b == {"software": [400, 100]}


def test_group_by_category_empty():
    result = group_by_category([])
    assert result == {}


# ---------- compute_totals ----------

def test_compute_totals():
    result = compute_totals(RECORDS_A)
    assert result == {"travel": 300, "food": 50}


# ---------- top_categories ----------

def test_top_categories_top_1():
    result = top_categories(RECORDS_A, 1)
    assert result == [("travel", 300)]


def test_top_categories_top_2():
    result = top_categories(RECORDS_A, 2)
    assert result == [("travel", 300), ("food", 50)]


def test_top_categories_zero():
    result = top_categories(RECORDS_A, 0)
    assert result == []
