"""
Solution to Day 3, Problem 1 
"""
from dataclasses import dataclass
from lib2to3.pgen2 import grammar
import click

def convert_symbols_and_numbers(data_item):

    if data_item.isdigit():
        return(int(data_item))
    else:
        return(data_item)
    

@dataclass
class NumberLocation:
    row: int
    col_start: int
    col_end: int


def get_number_locations(data):

    number_locations = []
    max_position = len(data[0]) - 1

    for row_number, row in enumerate(data):
        new_digit = True
        location_holder = NumberLocation(0, 0, 0)
        for position, item in enumerate(row):
            if item.isdigit() and new_digit:
                location_holder.row = row_number
                location_holder.col_start = position
                location_holder.col_end = position
                new_digit = False
            elif item.isdigit() and not new_digit:
                location_holder.col_end = position
                if position == max_position:
                    number_locations.append(location_holder)
            elif not item.isdigit() and location_holder != NumberLocation(0, 0, 0):
                number_locations.append(location_holder)
                location_holder = NumberLocation(0, 0, 0)
                new_digit = True


    return number_locations

def get_number(number_location, data):

    number = data[number_location.row][number_location.col_start:number_location.col_end+1]

    return number

def get_numbers(number_locations, data):

    all_numbers = [get_number(location, data) for location in number_locations]

    return all_numbers

def check_for_symbol(number_locations, data):

    valid_list = []
    for number in number_locations:
        row_idx = number.row
        number_start_idx = number.col_start
        number_end_idx = number.col_end

        row_length = len(data[row_idx])

        row_min = max(row_idx-1, 0)
        row_max = min(row_idx+2, len(data))
        col_min = max(number_start_idx-1, 0)
        col_max = min(number_end_idx+1, row_length)

        symbols_to_check = []
        for row in range(row_min, row_max):
            row_data_to_check = data[row][col_min:col_max+1]
            symbols_to_check.extend(row_data_to_check)

        valid = any((not(x.isdigit()) and x!=".") for x in symbols_to_check)

        valid_list.append(valid)

    return valid_list


def get_valid_numbers(all_numbers, valid_list):
    #valid_numbers = [467, 35, 633, 617, 592, 755, 655, 598]

    valid_numbers = [(''.join(number), validity) for number, validity in zip(all_numbers, valid_list)]
    valid_integers = [int(number) for number, validity in valid_numbers if validity]

    return valid_integers

def sum_numbers(numbers):
    total = sum(numbers)
    return total


def get_symbol_locations(symbol, data):

    symbol_locations = []

    for row_number, row in enumerate(data):
        for columnn_number, item in enumerate(row):
            if item == symbol:
                symbol_locations.append((row_number, columnn_number))

    return symbol_locations

def find_numbers_adjacent_to_symbols(symbol_locations, number_locations, data):

    symbol_numbers = []
    row_length = len(data[0])

    for symbol_row_number, symbol_column_number in symbol_locations:
        row_min = max(symbol_row_number-1, 0)
        row_max = min(symbol_row_number+1, row_length)
        col_min = max(symbol_column_number-1, 0)
        col_max = min(symbol_column_number+1, row_length)

        adjacent_numbers = []
        for number_location in number_locations:
            if row_min <= number_location.row <= row_max:

                digit_column_positions = range(number_location.col_start, number_location.col_end+1)
                digit_in_range = [col_min <= digit_col_position <= col_max for digit_col_position in digit_column_positions]
                if any(digit_in_range):
                    adjacent_numbers.append(int(''.join(get_number(number_location, data))))

        symbol_numbers.append(adjacent_numbers)

    return symbol_numbers

def calculate_gear_ratios(numbers_adjacent_to_symbols):

    gear_ratios = []
    for symbol_numbers in numbers_adjacent_to_symbols:
        if len(symbol_numbers) == 2:
            gear_ratio = symbol_numbers[0] * symbol_numbers[1]
            gear_ratios.append(gear_ratio)

    return gear_ratios


def problem_01(file):
    """Day 3, Problem 1"""

    with open(file, encoding="utf-8") as f:
        data = [[character for character in line.strip()] for line in f]

    number_locations = get_number_locations(data)

    all_numbers = get_numbers(number_locations, data)

    valid_list = check_for_symbol(number_locations, data)

    valid_numbers = get_valid_numbers(all_numbers, valid_list)

    answer = sum_numbers(valid_numbers)

    print(f"Answer for Day 3, Problem 1: {answer}")


def problem_02(file):
    """Day 3, Problem 2"""

    with open(file, encoding="utf-8") as f:
        data = [[character for character in line.strip()] for line in f]

    # Start with the locations of all numbers
    number_locations = get_number_locations(data)

    # Find the locations of all * symbols
    symbol_locations = get_symbol_locations("*", data)

    # Check how many numbers are directly adjacent to each symbol's location
    adjacent_numbers = find_numbers_adjacent_to_symbols(symbol_locations, number_locations, data)

    # If there are two numbers for a symbol, extract the numbers and multiply them to get the gear ratio
    gear_ratios = calculate_gear_ratios(adjacent_numbers)

    answer = sum_numbers(gear_ratios)

    print(f"Answer for Day 3, Problem 2: {answer}")
    


@click.command()
@click.option(
    "--file",
    default="aoc_2023/day_03/data/sample_1.txt",
)
def main(file):
    """Run the problem"""
    problem_01(file)

    problem_02(file)

    print("Finished")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
    