"""Tests for day 3, problem 1 and 2"""
import pytest
from tests.aoc_2023.day_03.mock_input import MockData, cases
from aoc_2023.day_03.problem import (
    get_number_locations,
    get_numbers,
    check_for_symbol,
    get_valid_numbers,
    sum_numbers,
    get_symbol_locations,
    find_numbers_adjacent_to_symbols,
    calculate_gear_ratios,
)

@pytest.mark.parametrize("case", cases)
def test_get_number_locations(case: MockData):
    number_locations = get_number_locations(case.data)
    number_location_tuples = [(loc.row, loc.col_start, loc.col_end) for loc in number_locations]

    assert number_location_tuples == [(loc.row, loc.col_start, loc.col_end) for loc in case.number_locations]

@pytest.mark.parametrize("case", cases)
def test_get_numbers(case: MockData):
    assert get_numbers(case.number_locations, case.data) == case.all_numbers

@pytest.mark.parametrize("case", cases)
def test_check_for_symbol(case: MockData):
    assert check_for_symbol(case.number_locations, case.data) == case.valid_list
