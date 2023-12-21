"""
Solution to Day 1, Problem 1 
"""
import click


def get_numbers(calibration_text: str) -> list[int]:
    """Get a list of digits from a calibration string"""
    numbers = [
        int(character) for character in calibration_text if character.isnumeric()
    ]

    return numbers


def get_calibration_value(numbers: list[int]) -> int:
    """Get the calibration value from a list of digits"""
    try:
        tens_digit = numbers[0]
        ones_digit = numbers[-1]
    except IndexError:
        print("The input contains a string with no numbers. Check the file.")
        tens_digit = 0
        ones_digit = 0

    calibration_value = tens_digit * 10 + ones_digit

    return calibration_value


@click.command()
@click.option(
    "--file",
    default="aoc_2023/day_01/data/input.txt",
)
def problem_01(file):
    """Day 1, Problem 1"""
    with open(file, encoding="utf-8") as f:
        calibration_numbers = [get_numbers(calibration_text) for calibration_text in f]

    calibration_values = [
        get_calibration_value(numbers) for numbers in calibration_numbers
    ]

    answer = sum(calibration_values)

    print(answer)


if __name__ == "__main__":
    problem_01()  # pylint: disable=no-value-for-parameter
