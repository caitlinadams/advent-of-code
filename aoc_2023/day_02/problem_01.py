"""
Solution to Day 1, Problem 1 
"""
import click

# Problem characteristics
# There are 100 games, and each line starts with "Game n:"
# where n is between 1 and 100 with no leading zeros
# Each game lists m draws, with each draw separated by a semi colon.
# A draw is made up of at least 1, but up to 3 cube colours, proceeded
# by the number of cubes drawn of that colour
# cubes can only be red, green or blue
# The goal is to identify which games are possible and which are impossible
# if there are 12 red cubes, 13 green cubes, and 14 blue cubes
# The solution is the sum of the Game IDs for possible games

# Possible structure
# Build a pandas dataframe using
# Game ID, Draw ID, n_red, n_blue, n_green
# Then, look at all n_red for a given draw; if any are greater than 12, the game is impossible
# Alternatively, if all are under 12, the game is possible.
# For one game, there need only be one impossible draw to invalidate the game
# Things are generally separated by spaces, so could use this as a delimiter.
# Need to keep numbers and colours together
# Could also keep the maximum red, green and blue value for any game and only test these
# If the max is under the limit, then all other values are fine


def get_game_id(game: str) -> int:
    """Get the game ID"""

    game = game.rstrip()

    game_label, _ = game.split(": ")

    _, game_id = game_label.split(" ")

    game_id_int = int(game_id)

    return game_id_int


def get_game_draws(game: str) -> dict[int, str]:
    """Given a game string, extract the draws as a dictionary"""

    game = game.rstrip()

    _, draws = game.split(": ")

    draw_results = dict(enumerate(draws.split("; ")))

    return draw_results


def get_game_colour_counts(draws: dict[int, str]):
    """Get a list of cubes of each colour from all draws"""

    single_draw_results = [
        colour_count.split(" ")
        for draw_results in draws.values()
        for colour_count in draw_results.split(", ")
    ]

    colours = list(set(result[1] for result in single_draw_results))

    colour_counts = {
        colour: [
            int(result[0]) for result in single_draw_results if result[1] == colour
        ]
        for colour in colours
    }

    return colour_counts


def get_max_colour_counts_per_game(
    colour_counts: dict[str, list[int]]
) -> dict[str, int]:
    """For a collection of draws from a game, find the maximum number of each colour drawn"""

    max_colour_counts = {
        colour: max(counts) for colour, counts in colour_counts.items()
    }

    return max_colour_counts


def check_possible(
    max_colour_counts: dict[str, int], bag_contents: dict[str, int]
) -> int:
    """For a given number of cubes drawn per colour, assess whether it's possible to draw that many from the bag's contents"""

    count_possible_from_contents = [
        max_colour_counts[colour] <= bag_contents[colour]
        for colour in max_colour_counts.keys()
    ]

    possible = all(count_possible_from_contents)

    return possible


def get_cube_of_max_counts(max_colour_counts: dict[str, int]) -> int:
    """Multiply the maximum number of cubes together for each colour"""

    cubed = 1
    for colour in max_colour_counts.keys():
        cubed = cubed * max_colour_counts[colour]

    return cubed


# def validate_game(game, bag_contents):
#     """Return game id and 1 for valid, 0 for invalid"""

#     game_id_int, colours, draw_results = get_game_data(game)

#     max_draws = get_max_draws_per_colour(colours, draw_results)

#     possible = check_possible(max_draws, bag_contents)

#     return (game_id_int, possible)


def problem_01(file):
    """Day 2, Problem 1"""

    bag_contents = {"red": 12, "green": 13, "blue": 14}

    with open(file, encoding="utf-8") as f:
        games = list(f)

    ids = [get_game_id(game) for game in games]
    draws = [get_game_draws(game) for game in games]
    game_colour_counts = [get_game_colour_counts(draw) for draw in draws]
    game_colour_counts_max = [
        get_max_colour_counts_per_game(count) for count in game_colour_counts
    ]
    possible = [
        check_possible(counts_max, bag_contents)
        for counts_max in game_colour_counts_max
    ]

    answer = sum([game_id * allowed for game_id, allowed in zip(ids, possible)])

    print(f"Answer for Day 2, Problem 1: {answer}")


def problem_02(file):
    """Day 2, Problem 2"""

    with open(file, encoding="utf-8") as f:
        games = list(f)

    draws = [get_game_draws(game) for game in games]
    game_colour_counts = [get_game_colour_counts(draw) for draw in draws]
    game_colour_counts_max = [
        get_max_colour_counts_per_game(count) for count in game_colour_counts
    ]

    cubed_values = [
        get_cube_of_max_counts(max_counts) for max_counts in game_colour_counts_max
    ]

    answer = sum(cubed_values)

    print(f"Answer for Day 2, Problem 2: {answer}")


@click.command()
@click.option(
    "--file",
    default="aoc_2023/day_02/data/input.txt",
)
def main(file):
    """Run both problems"""
    problem_01(file)
    problem_02(file)

    print("Finished")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
