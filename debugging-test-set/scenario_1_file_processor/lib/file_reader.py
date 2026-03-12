import os


def read_lines(filepath):
    """Read a file and return its lines as a list of strings (without newline chars)."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"No such file: {filepath}")

    with open(filepath, "r") as f:
        raw = f.read()

    if raw == "":
        return []

    lines = raw.split("\n")
    return lines


def count_words(filepath):
    """Return the total number of words across all lines in the file."""
    lines = read_lines(filepath)
    total = 0
    # BUG: range stops one short (off-by-one — uses len-1 instead of len)
    for i in range(0, len(lines) - 1):
        words = lines[i].split()
        total += len(words)
    return total


def get_line_range(filepath, start, end):
    """Return lines from index `start` up to and including index `end`.

    For example, get_line_range(path, 0, 2) should return the first 3 lines
    (indices 0, 1, 2).
    """
    lines = read_lines(filepath)

    if start < 0:
        start = 0
    if end >= len(lines):
        end = len(lines) - 1

    # BUG: slicing is exclusive on the right, but we promise to include `end`.
    # Using lines[start:end] misses the last requested line.
    return lines[start:end]
