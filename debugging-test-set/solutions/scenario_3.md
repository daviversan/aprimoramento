# Scenario 3 — Ledger & Fee Calculator — Solution

## Bug 1: Transfer signs are inverted in `Ledger.transfer`

**File:** `lib/ledger.py`, method `Ledger.transfer`

**Symptom:** After transferring 200 from "checking" to "vendor", checking
goes UP to 1200 and vendor goes DOWN to -200.

**Root cause:** The code does `src.balance += amount` (should subtract) and
`dst.balance -= amount` (should add). The operations are backwards.

**Fix:**

```python
# Before
src.balance += amount
dst.balance -= amount

# After
src.balance -= amount
dst.balance += amount
```

---

## Bug 2: Tax applied to wrong base in `calculate_total_with_tax`

**File:** `lib/calculator.py`, function `calculate_total_with_tax`

**Symptom:** `calculate_total_with_tax(1000, 0.02, 0.10)` returns 1120
instead of 1022. The tax is calculated on the full amount instead of on the fee.

**Root cause:** `tax = amount * tax_rate` should be `tax = fee * tax_rate`.
The docstring is clear that tax is on the fee, not the amount.

**Fix:**

```python
# Before
tax = amount * tax_rate

# After
tax = fee * tax_rate
```

---

## Bug 3: Integer division in `split_expense`

**File:** `lib/calculator.py`, function `split_expense`

**Symptom:** `split_expense(100, 3)` returns 33 instead of 33.33.

**Root cause:** The code uses `//` (floor division) instead of `/` (true
division). Floor division truncates the decimal part.

**Fix:**

```python
# Before
per_person = total // num_people

# After
per_person = total / num_people
```
