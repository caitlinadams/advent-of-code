"""
Mock data for day 2, problem 1
Allowed colour draws: only 12 red cubes, 13 green cubes, and 14 blue cubes
"""
import dataclasses


bag_contents = {"red": 12, "green": 13, "blue": 14}


@dataclasses.dataclass
class MockData:
    """Class to contain data example with 1,0 for possible"""

    game: str
    game_id: int
    draws: dict[int, str]
    colour_counts: dict[str, list[int]]
    max_colour_counts: dict[str, int]
    max_counts_cubed: int
    possible: int


case_1 = MockData(
    game="Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    draws={0: "3 blue, 4 red", 1: "1 red, 2 green, 6 blue", 2: "2 green"},
    colour_counts={"red": [4, 1], "blue": [3, 6], "green": [2, 2]},
    max_colour_counts={"red": 4, "blue": 6, "green": 2},
    max_counts_cubed=48,
    game_id=1,
    possible=1,
)

case_2 = MockData(
    game="Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    draws={0: "1 blue, 2 green", 1: "3 green, 4 blue, 1 red", 2: "1 green, 1 blue"},
    colour_counts={"red": [1], "blue": [1, 4, 1], "green": [2, 3, 1]},
    max_colour_counts={"red": 1, "blue": 4, "green": 3},
    max_counts_cubed=12,
    game_id=2,
    possible=1,
)

case_3 = MockData(
    game="Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    draws={
        0: "8 green, 6 blue, 20 red",
        1: "5 blue, 4 red, 13 green",
        2: "5 green, 1 red",
    },
    colour_counts={"red": [20, 4, 1], "blue": [6, 5], "green": [8, 13, 5]},
    max_colour_counts={"red": 20, "blue": 6, "green": 13},
    max_counts_cubed=1560,
    game_id=3,
    possible=0,
)

case_4 = MockData(
    game="Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    draws={
        0: "1 green, 3 red, 6 blue",
        1: "3 green, 6 red",
        2: "3 green, 15 blue, 14 red",
    },
    colour_counts={"red": [3, 6, 14], "blue": [6, 15], "green": [1, 3, 3]},
    max_colour_counts={"red": 14, "blue": 15, "green": 3},
    max_counts_cubed=630,
    game_id=4,
    possible=0,
)

case_5 = MockData(
    game="Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    draws={0: "6 red, 1 blue, 3 green", 1: "2 blue, 1 red, 2 green"},
    colour_counts={"red": [6, 1], "blue": [1, 2], "green": [3, 2]},
    max_colour_counts={"red": 6, "blue": 2, "green": 3},
    max_counts_cubed=36,
    game_id=5,
    possible=1,
)

cases = [case_1, case_2, case_3, case_4, case_5]
