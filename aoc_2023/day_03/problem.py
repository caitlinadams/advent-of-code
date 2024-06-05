"""
Solution to Day 3, Problem 1 
"""
from dataclasses import dataclass
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

    new_digit = True
    location_holder = NumberLocation(0, 0, 0)
    number_locations = []

    for row_number, row in enumerate(data):
        for position, item in enumerate(row):
            if item.isdigit() and new_digit:
                location_holder.row = row_number
                location_holder.col_start = position
                new_digit = False
            elif item.isdigit() and not new_digit:
                location_holder.col_end = position
            elif not item.isdigit() and location_holder != NumberLocation(0, 0, 0):
                number_locations.append(location_holder)
                location_holder = NumberLocation(0, 0, 0)
                new_digit = True

    return number_locations

def get_numbers(number_locations, data):

    all_numbers = [data[location.row][location.col_start:location.col_end+1] for location in number_locations]

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

        valid = any((not(x.isdigit() or x==".") for x in symbols_to_check))

        valid_list.append(valid)

    return valid_list



def get_valid_numbers(data):
    #valid_numbers = [467, 35, 633, 617, 592, 755, 655, 598]

    number_locations = get_number_locations(data)
    all_numbers = get_numbers(number_locations, data)
    valid_list = check_for_symbol(number_locations, data)

    valid_numbers = [number for number, validity in zip(all_numbers, valid_list) if validity]
    valid_integers = [int(''.join(valid_number_list)) for valid_number_list in valid_numbers]

    return valid_integers

def sum_numbers(numbers):
    total = sum(numbers)
    return total




def problem_01(file):
    """Day 3, Problem 1"""

    with open(file, encoding="utf-8") as f:
        data = [[character for character in line.strip()] for line in f]

    valid_numbers = get_valid_numbers(data)

    answer = sum_numbers(valid_numbers)

    print(f"Answer for Day 3, Problem 1: {answer}")

@click.command()
@click.option(
    "--file",
    default="aoc_2023/day_03/data/input.txt",
)
def main(file):
    """Run the problem"""
    problem_01(file)

    print("Finished")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
    