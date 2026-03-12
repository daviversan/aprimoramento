# Scenario 1 — File Processor

## Business context

You inherited a small utility that reads a text file and returns statistics about its
contents: the lines as a list, total word count, and the ability to extract a specific
range of lines. The test suite has several tests — some pass, some fail.

## Your task

Find and fix the logic bugs so that **all** tests pass. There are **2 bugs** in the code.

## Running the tests

```bash
cd scenario_1_file_processor
pytest
```

Or from the repo root:

```bash
pytest scenario_1_file_processor/
```

## Time target

~15-20 minutes.

## Reminder

Use the systematic framework from [DEBUGGING_FRAMEWORK.md](../DEBUGGING_FRAMEWORK.md).
Talk through your reasoning out loud.
