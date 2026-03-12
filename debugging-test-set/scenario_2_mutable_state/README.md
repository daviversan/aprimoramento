# Scenario 2 — Mutable State Aggregator

## Business context

You inherited a data aggregation module used to group transaction records by
category and compute running totals. The module is called repeatedly across
different datasets — each call should be independent. The test suite has several
tests — some pass, some fail.

## Your task

Find and fix the logic bugs so that **all** tests pass. There are **2 bugs** in the code.

## Running the tests

```bash
cd scenario_2_mutable_state
pytest
```

Or from the repo root:

```bash
pytest scenario_2_mutable_state/
```

## Time target

~15-20 minutes.

## Reminder

Use the systematic framework from [DEBUGGING_FRAMEWORK.md](../DEBUGGING_FRAMEWORK.md).
Talk through your reasoning out loud.
