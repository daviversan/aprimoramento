# Brex-Style Debugging Interview Prep

This project simulates the Brex Software Engineering Internship debugging interview.
Each scenario contains a small Python codebase with **logic bugs** (no syntax errors)
that you must find and fix under time pressure, just like the real interview.

## Setup

```bash
pip install -r requirements.txt
```

## How to practice

1. **Set a timer** for 45-60 minutes (the real interview is ~45 min).
2. **Pick a scenario** (start with scenario 1 if this is your first run).
3. **Run the tests** to see which ones fail:
   ```bash
   pytest scenario_1_file_processor/
   ```
4. **Use the systematic framework** described in [DEBUGGING_FRAMEWORK.md](DEBUGGING_FRAMEWORK.md).
5. **Talk out loud** as if an interviewer is watching — vocalize your hypothesis before changing code.
6. **Fix the bugs** with minimal changes. Re-run the **full** test suite after each fix to check for regressions.
7. **Check your work** against the solution notes in `solutions/` only after you are done.

## Scenarios

| # | Folder | Domain | Bugs | Target time |
|---|--------|--------|------|-------------|
| 1 | `scenario_1_file_processor/` | File reading, line/word counting | 2 | ~15-20 min |
| 2 | `scenario_2_mutable_state/` | Data aggregation with lists/dicts | 2 | ~15-20 min |
| 3 | `scenario_3_ledger/` | Financial ledger & fee calculations | 3 | ~20-25 min |
| 4 | `scenario_4_spend_report/` | Corporate spend analytics report | 3 | ~25-30 min |

## Rules (mirror the real interview)

- **No AI or GitHub Copilot.** You may look up Python documentation online.
- Bugs are **logic-based**, not syntax errors. The code runs — it just produces wrong results.
- Use `print()` statements or `breakpoint()` / `pdb` to inspect state.
- Make the **smallest fix** that corrects the logic. Do not rewrite entire functions.

## Running all scenarios at once

```bash
pytest
```

This runs every test in the repo. Some tests pass and some fail — your job is to make them all pass.
