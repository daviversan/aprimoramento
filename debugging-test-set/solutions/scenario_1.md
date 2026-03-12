# Scenario 1 — File Processor — Solution

## Bug 1: `count_words` skips the last line (off-by-one)

**File:** `lib/file_reader.py`, function `count_words`

**Symptom:** `count_words("sample.txt")` returns 9 instead of 14 — the words
on the last line are never counted.

**Root cause:** The loop uses `range(0, len(lines) - 1)`, which excludes the
last index. For a list of 5 elements (indices 0-4), this iterates 0-3.

**Fix:** Change the range to `range(len(lines))` (or `range(0, len(lines))`):

```python
# Before
for i in range(0, len(lines) - 1):

# After
for i in range(len(lines)):
```

---

## Bug 2: `get_line_range` excludes the end index (slice boundary)

**File:** `lib/file_reader.py`, function `get_line_range`

**Symptom:** `get_line_range(path, 1, 3)` returns 2 lines instead of 3.
The docstring promises inclusive `end`, but the slice `[start:end]` is exclusive
on the right.

**Root cause:** Python slicing `[start:end]` does not include the element at
index `end`. The function should use `[start:end + 1]`.

**Fix:**

```python
# Before
return lines[start:end]

# After
return lines[start:end + 1]
```
