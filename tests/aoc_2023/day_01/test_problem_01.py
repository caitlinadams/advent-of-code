"""Tests for day 1, problem 1"""
from hypothesis import given, strategies as st
from aoc_2023.day_01.problem_01 import get_numbers, get_calibration_value


@given(st.text(alphabet=st.characters(categories=["L", "Nd"])))
def test_get_numbers(t):
    """
    Test for function to get numbers from calibration text
    Test produces a string containing only letters (L) and
    decimal digits (Nd)
    """
    assert get_numbers(t) == [int(x) for x in t if x.isnumeric()]


@given(st.lists(st.integers(min_value=0, max_value=9)))
def test_get_calibration_value(l):
    """Test for function to get calibration value from list of digits"""
    try:
        ten_value = l[0]
        one_value = l[-1]
    except IndexError:
        ten_value = ""
        one_value = 0

    assert get_calibration_value(l) == int(f"{ten_value}{one_value}")
