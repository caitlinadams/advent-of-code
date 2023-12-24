"""Tests for day 2, problem 1"""
import pytest
from tests.aoc_2023.day_02.mock_input import MockData, cases, bag_contents
from aoc_2023.day_02.problem_01 import (
    get_game_id,
    get_game_draws,
    get_game_colour_counts,
    get_max_colour_counts_per_game,
    check_possible,
)


@pytest.mark.parametrize("case", cases)
def test_game_id(case: MockData):
    """Tests for get_game_id function"""
    assert get_game_id(case.game) == case.game_id


@pytest.mark.parametrize("case", cases)
def test_game_draws(case: MockData):
    """Tests for get_game_draws function"""
    assert get_game_draws(case.game) == case.draws


@pytest.mark.parametrize("case", cases)
def test_colour_counts(case: MockData):
    """Tests for get_game_colour_counts function"""
    assert get_game_colour_counts(case.draws) == case.colour_counts


@pytest.mark.parametrize("case", cases)
def test_max_colour_counts(case: MockData):
    """Tests for get_max_colour_counts_per_game"""
    assert get_max_colour_counts_per_game(case.colour_counts) == case.max_colour_counts


@pytest.mark.parametrize("case", cases)
def test_possible(case: MockData):
    """Tests for check_possible function"""
    assert check_possible(case.max_colour_counts, bag_contents) == case.possible
