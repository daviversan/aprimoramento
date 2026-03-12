# Systematic Debugging Framework

Use this checklist during every scenario. The goal is to be **deterministic**, not lucky.

## The 5-Phase Loop

### Phase 1 — Reproduce

- Run `pytest test/` and read the output carefully.
- Note **which tests fail** and which **pass** (passing tests are clues too).
- Write down the **exact delta**: expected value vs. actual value.

### Phase 2 — Isolate

- Trace the data flow from the failing test's input through the code.
- **Bisect strategy**: place a `print()` at the midpoint of the pipeline.
  - If the value is correct there, the bug is in the second half.
  - If wrong, the bug is in the first half.
- Repeat until you have narrowed it to 1-2 functions or lines.

### Phase 3 — Hypothesize

- State your hypothesis in **one sentence** before touching any logic:
  > "I believe the loop is skipping the last element because the range
  > endpoint is exclusive and we need `<=` instead of `<`."
- Say it out loud (or write it down) — this is what the interviewer evaluates.

### Phase 4 — Verify (before fixing)

- Add a `print()` or `logging.debug()` immediately before and after the
  suspected line to confirm the state matches your hypothesis.
- **Do not change logic yet.** Verify first.

### Phase 5 — Fix and Regress

- Make the **smallest** change that corrects the flaw.
- Re-run the **entire** test suite (`pytest`), not just the one test you were looking at.
- If a previously passing test now fails, you introduced a **regression** — undo and rethink.

## Communication Tips

| Do | Don't |
|----|-------|
| "I see the test expects 100 but gets 120 — let me trace where 120 comes from." | Silently stare at the code for 3 minutes. |
| "My hypothesis is X. I'll add a print here to confirm." | Randomly change operators hoping the test passes. |
| "I've been stuck for 5 minutes — can I get a hint on how this class models the data?" | Stubbornly refuse to ask for help until time runs out. |
| "Let me re-run all tests to make sure I didn't break anything." | Fix one test and move on without checking the rest. |

## Quick `print()` Patterns

```python
# Show variable name and value together
print(f"{total=}")           # Python 3.8+  ->  total=42

# Show type to catch int-vs-float or None surprises
print(f"{type(amount)=}")

# Mark a branch to see if it executes
print(">>> ENTERED the discount branch")

# Dump a list mid-loop
for i, item in enumerate(items):
    print(f"  [{i}] {item=}")
```

## Quick `pdb` Reference (optional — use print if faster for you)

```python
breakpoint()   # drops into interactive debugger
# p variable   — print a variable
# n            — next line (step over)
# s            — step into function call
# c            — continue to next breakpoint
# l            — list source around current line
# w            — show call stack
```
