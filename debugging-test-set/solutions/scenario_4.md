# Scenario 4 — Corporate Spend Report — Solution

## Bug 1: `filter_by_date_range` excludes end_date (strict inequality)

**File:** `lib/spend_report.py`, function `filter_by_date_range`

**Symptom:** Filtering with `end_date = date(2025, 3, 20)` does not include the
expense on that exact date. `test_filter_boundary_inclusive` fails.

**Root cause:** The condition uses `exp["date"] < end_date` (strict less-than)
instead of `<=`. The docstring says both boundaries are inclusive.

**Fix:**

```python
# Before
if exp["date"] >= start_date and exp["date"] < end_date:

# After
if exp["date"] >= start_date and exp["date"] <= end_date:
```

---

## Bug 2: `category_summary` sums amounts instead of counting transactions

**File:** `lib/spend_report.py`, function `category_summary`

**Symptom:** `category_summary(EXPENSES)` returns large numbers (e.g.
`{"travel": 2450, ...}`) instead of small counts like `{"travel": 3, ...}`.

**Root cause:** The code does `summary[cat] += exp["amount"]` instead of
`summary[cat] += 1`. It accumulates money instead of counting transactions.

**Fix:**

```python
# Before
summary[cat] += exp["amount"]

# After
summary[cat] += 1
```

---

## Bug 3: `flag_over_budget` sorts ascending instead of descending

**File:** `lib/spend_report.py`, function `flag_over_budget`

**Symptom:** `flag_over_budget(EXPENSES, 500)` returns `[950, 1200]` instead
of `[1200, 950]`. The order is reversed.

**Root cause:** `flagged.sort(key=lambda x: x["amount"])` sorts ascending by
default. The function should return highest-first (descending).

**Fix:**

```python
# Before
flagged.sort(key=lambda x: x["amount"])

# After
flagged.sort(key=lambda x: x["amount"], reverse=True)
```
