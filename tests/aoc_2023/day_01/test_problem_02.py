"""Tests for day 1, problem 2"""
import pytest
from tests.aoc_2023.day_01.mock_input import (
    case_1,
    case_2,
    case_3,
    case_4,
    case_5,
    case_6,
    case_7,
    case_8,
)
from aoc_2023.day_01.problem_02 import (
    find_all,
    get_numbers_words_digits,
    get_calibration_value,
)

test_cases = [case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8]


class TestFindall:
    """Tests for find_all function"""

    def test_case1(self):
        """Test 1 for find_all function"""
        assert list(find_all("two", case_1[0])) == [0]

    def test_case2(self):
        """Test 2 for find_all function"""
        assert list(find_all("three", case_2[0])) == [7]

    def test_case8(self):
        """Test 8 for find_all function"""
        assert list(find_all("three", case_8[0])) == [0, 6]


class TestGetnumberswordsdigits:
    """Tests for get_numbers_words_digits function"""

    @pytest.mark.parametrize("case", test_cases)
    def test_cases(self, case: tuple):
        """Test for get_numbers_words_digits function"""
        assert get_numbers_words_digits(case[0]) == case[1]


class TestGetcalibrationvalue:
    """Tests for get_calibration_value function"""

    @pytest.mark.parametrize("case", test_cases)
    def test_cases(self, case: tuple):
        """Test for get_calibration_value function"""
        assert get_calibration_value(case[1]) == case[2]
