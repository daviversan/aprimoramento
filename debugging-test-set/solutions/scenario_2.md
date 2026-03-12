# Scenario 2 — Mutable State Aggregator — Solution

## Bug 1: Mutable default argument in `group_by_category`

**File:** `lib/aggregator.py`, function `group_by_category`

**Symptom:** The second call to `group_by_category` still contains data from
the first call. `test_group_by_category_independent_calls` fails because
`result_b` contains categories from `RECORDS_A` as well.

**Root cause:** The default parameter `groups={}` is evaluated once at function
definition time. Every call that doesn't pass an explicit `groups` argument
shares the same dict object, so data leaks between calls.

**Fix:** Use `None` as the default and create a new dict inside the function:

```python
# Before
def group_by_category(records, groups={}):

# After
def group_by_category(records, groups=None):
    if groups is None:
        groups = {}
```

---

## Bug 2: `top_categories` returns n-1 items instead of n

**File:** `lib/aggregator.py`, function `top_categories`

**Symptom:** `top_categories(records, 2)` returns only 1 result instead of 2.

**Root cause:** The slice uses `[:n - 1]` instead of `[:n]`. For `n=1` this
returns an empty list; for `n=2` it returns 1 item.

**Fix:**

```python
# Before
return sorted_cats[: n - 1] if n > 0 else []

# After
return sorted_cats[:n] if n > 0 else []
```
