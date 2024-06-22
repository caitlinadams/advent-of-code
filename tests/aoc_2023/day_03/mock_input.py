"""
Mock data for day 3, problem 1 and 2
"""
import dataclasses

def read_input(file):
    with open(file, encoding="utf-8") as f:
        data = [[character for character in line.strip()] for line in f]

    return data

@dataclasses.dataclass(eq=True, frozen=True)
class NumberLocation:
    row: int
    col_start: int
    col_end: int

@dataclasses.dataclass
class MockData:
    """Class to contain test data"""

    data: list[list[str]]
    number_locations: list[NumberLocation]
    all_numbers: list[list[str]]
    valid_numbers: list[int]
    valid_list: list[bool]
    answer_1: int
    symbol_locations: list[tuple[int, int]]
    adjacent_numbers: list[list[int]]
    gear_ratios: list[int]
    answer_2: int

case1 = MockData(
    data=[
        ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
        ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'], 
        ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.']
    ],
    number_locations=[
        NumberLocation(row=0, col_start=0, col_end=2),
        NumberLocation(row=0, col_start=5, col_end=7),
        NumberLocation(row=2, col_start=2, col_end=3),
        NumberLocation(row=2, col_start=6, col_end=8),
        NumberLocation(row=4, col_start=0, col_end=2)
    ],
    all_numbers=[['4', '6', '7'], ['1', '1', '4'], ['3', '5'], ['6', '3', '3'], ['6', '1', '7']],
    valid_numbers=[467, 35, 633, 617],
    valid_list=[True, False, True, True, True],
    answer_1=1717,
    symbol_locations=[(1, 3), (4, 3)],
    adjacent_numbers=[[467, 35], [617]],
    gear_ratios=[16345],
    answer_2=16345
)

cases = [case1]