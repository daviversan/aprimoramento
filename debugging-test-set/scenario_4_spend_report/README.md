# Scenario 4 — Corporate Spend Report

## Business context

You inherited a spend analytics module used by a fintech company's dashboard.
It processes a list of employee expense transactions and generates summary reports:
filtering by date range, categorizing expenses, computing per-employee totals, and
flagging transactions that exceed a budget threshold.

The test suite has several tests — some pass, some fail.

## Your task

Find and fix the logic bugs so that **all** tests pass. There are **3 bugs** in
the code. Fixing one bug may reveal failures in tests that previously appeared
to pass, so always re-run the full suite.

## Running the tests

```bash
cd scenario_4_spend_report
pytest
```

Or from the repo root:

```bash
pytest scenario_4_spend_report/
```

## Time target

~25-30 minutes.

## Reminder

Use the systematic framework from [DEBUGGING_FRAMEWORK.md](../DEBUGGING_FRAMEWORK.md).
Talk through your reasoning out loud.
