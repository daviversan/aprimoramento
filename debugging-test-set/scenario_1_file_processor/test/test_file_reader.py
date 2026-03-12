import os
import sys

_scenario_dir = os.path.join(os.path.dirname(__file__), "..")
for _key in list(sys.modules.keys()):
    if _key == "lib" or _key.startswith("lib."):
        del sys.modules[_key]
if _scenario_dir not in sys.path:
    sys.path.insert(0, _scenario_dir)

from lib.file_reader import read_lines, count_words, get_line_range

INPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "input")


def _path(filename):
    return os.path.join(INPUT_DIR, filename)


# ---------- read_lines ----------

def test_read_lines_returns_all_lines():
    lines = read_lines(_path("sample.txt"))
    assert lines == [
        "hello world",
        "foo bar baz",
        "python is great",
        "one",
        "the quick brown fox jumps",
    ]


def test_read_lines_empty_file():
    lines = read_lines(_path("empty.txt"))
    assert lines == []


def test_read_lines_single_line():
    lines = read_lines(_path("single_line.txt"))
    assert lines == ["only one line here"]


# ---------- count_words ----------

def test_count_words_sample():
    """sample.txt has 2 + 3 + 3 + 1 + 5 = 14 words."""
    assert count_words(_path("sample.txt")) == 14


def test_count_words_single_line():
    """single_line.txt has 4 words."""
    assert count_words(_path("single_line.txt")) == 4


def test_count_words_empty_file():
    assert count_words(_path("empty.txt")) == 0


# ---------- get_line_range ----------

def test_get_line_range_full():
    result = get_line_range(_path("sample.txt"), 0, 4)
    assert result == [
        "hello world",
        "foo bar baz",
        "python is great",
        "one",
        "the quick brown fox jumps",
    ]


def test_get_line_range_subset():
    result = get_line_range(_path("sample.txt"), 1, 3)
    assert result == ["foo bar baz", "python is great", "one"]


def test_get_line_range_single_element():
    result = get_line_range(_path("sample.txt"), 2, 2)
    assert result == ["python is great"]
