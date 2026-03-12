# Scenario 3 — Ledger & Fee Calculator

## Business context

You inherited a small financial ledger module used inside a fintech company.
It tracks accounts with balances, processes debit/credit transactions, and
calculates fees and taxes on transactions. The test suite has several tests —
some pass, some fail.

## Your task

Find and fix the logic bugs so that **all** tests pass. There are **3 bugs**
across the two source files (`ledger.py` and `calculator.py`).

## Running the tests

```bash
cd scenario_3_ledger
pytest
```

Or from the repo root:

```bash
pytest scenario_3_ledger/
```

## Time target

~20-25 minutes.

## Reminder

Use the systematic framework from [DEBUGGING_FRAMEWORK.md](../DEBUGGING_FRAMEWORK.md).
Talk through your reasoning out loud.
