"""
Solution to Day 1, Problem 2
"""
import click


def find_all(substring, string):
    """Generator that yields the index of the substring in the string"""
    i = string.find(substring)
    while i != -1:
        yield i
        i = string.find(substring, i + 1)


def get_numbers_words_digits(calibration_text: str) -> list:
    """Get a list of digits from a calibration string"""
    number_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    valid_number_strings = list(number_words.keys()) + [
        str(number) for number in list(number_words.values())
    ]

    numbers = [
        (i, p)
        for p in valid_number_strings
        for i in find_all(p, calibration_text)
        if p in calibration_text
    ]

    sorted_numbers = [number for (index, number) in sorted(numbers, key=lambda x: x[0])]

    sorted_numbers_decimal = [
        number_words[number] if number in number_words else int(number)
        for number in sorted_numbers
    ]

    return sorted_numbers_decimal


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
def problem_02(file):
    """Day 1, Problem 2"""

    with open(file, encoding="utf-8") as f:
        calibration_strings = list(f)

    calibration_numbers = [
        get_numbers_words_digits(calibration_text)
        for calibration_text in calibration_strings
    ]

    calibration_values = [
        get_calibration_value(numbers) for numbers in calibration_numbers
    ]

    answer = sum(calibration_values)

    print(answer)


if __name__ == "__main__":
    problem_02()  # pylint: disable=no-value-for-parameter
