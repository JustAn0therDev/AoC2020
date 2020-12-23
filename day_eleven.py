from copy import copy
from typing import List, Tuple

problem_input = []
not_stabilized = True
ans = 0
is_part_two = True

# with open('dayeleven_input_sample.txt', 'r') as reader:
with open('dayeleven_input.txt', 'r') as reader:
    for line in reader:
        if line != '\n':
            problem_input.append(line.replace('\n', ''))

def check_current_seat(item: str, occupied_count: int, empty_count: int) -> Tuple[int, int]:
    if item == "#":
        occupied_count += 1
    elif item == 'L':
        empty_count += 1

    return occupied_count, empty_count

def check_current_seat_part_two(item: str, occupied_count: int, empty_count: int) -> Tuple[int, int, bool]:
    is_seat = item != '.'
    if item == "#":
        occupied_count += 1
    else:
        empty_count += 1

    return occupied_count, empty_count, is_seat

def can_go_up(current_row_index):
    return current_row_index >= 0

def can_go_left(current_column_index):
    return current_column_index >= 0

def can_go_right(current_column_index, column_index_limit):
    return current_column_index <= column_index_limit

def can_go_down(current_row_index, row_index_limit):
    return current_row_index <= row_index_limit

def print_grid(grid_input):
    print("GRID:")
    for i, _ in enumerate(grid_input):
        for j, _ in enumerate(grid_input[i]):
            print(grid_input[i][j], end='')
        print('\n')

""" 
    Each direction must know its limit for us to be able to check for every point available without bumping into some 
    index out of bounds exception
"""
def check_visible_seats(problem_input: list, occupied_count: int, empty_count: int, row_index: int, column_index: int, row_index_limit: int, column_index_limit: int) -> Tuple[int, int]:
    
    for i in range(0, 8):
        current_row_index = row_index
        current_column_index = column_index
        # up
        if i == 0:
            current_row_index -= 1
            while can_go_up(current_row_index):
                occupied_count, empty_count, is_seat = check_current_seat_part_two(problem_input[current_row_index][current_column_index], occupied_count, empty_count)
                if is_seat:
                    break
                current_row_index -= 1
        # up and right
        elif i == 1:
            current_column_index += 1
            current_row_index -= 1
            while can_go_up(current_row_index) and can_go_right(current_column_index, column_index_limit):
                occupied_count, empty_count, is_seat = check_current_seat_part_two(problem_input[current_row_index][current_column_index], occupied_count, empty_count)
                if is_seat:
                    break
                current_column_index += 1
                current_row_index -= 1
        # right
        elif i == 2:
            current_column_index += 1
            while can_go_right(current_column_index, column_index_limit):
                occupied_count, empty_count, is_seat = check_current_seat_part_two(problem_input[current_row_index][current_column_index], occupied_count, empty_count)
                if is_seat:
                    break
                current_column_index += 1
        # right and down
        elif i == 3:
            current_column_index += 1
            current_row_index += 1
            while can_go_right(current_column_index, column_index_limit) and can_go_down(current_row_index, row_index_limit):
                occupied_count, empty_count, is_seat = check_current_seat_part_two(problem_input[current_row_index][current_column_index], occupied_count, empty_count)
                if is_seat:
                    break
                current_column_index += 1
                current_row_index += 1
        # down
        elif i == 4:
            current_row_index += 1
            while can_go_down(current_row_index, row_index_limit):
                occupied_count, empty_count, is_seat = check_current_seat_part_two(problem_input[current_row_index][current_column_index], occupied_count, empty_count)
                if is_seat:
                    break
                current_row_index += 1
        # down and left
        elif i == 5:
            current_column_index -= 1
            current_row_index += 1
            while can_go_down(current_row_index, row_index_limit) and can_go_left(current_column_index):
                occupied_count, empty_count, is_seat = check_current_seat_part_two(problem_input[current_row_index][current_column_index], occupied_count, empty_count)
                if is_seat:
                    break
                current_column_index -= 1
                current_row_index += 1
        # left
        elif i == 6:
            current_column_index -= 1
            while can_go_left(current_column_index):
                occupied_count, empty_count, is_seat = check_current_seat_part_two(problem_input[current_row_index][current_column_index], occupied_count, empty_count)
                if is_seat:
                    break
                current_column_index -= 1
        # left and up
        elif i == 7:
            current_column_index -= 1
            current_row_index -= 1
            while can_go_left(current_column_index) and can_go_up(current_row_index):
                occupied_count, empty_count, is_seat = check_current_seat_part_two(problem_input[current_row_index][current_column_index], occupied_count, empty_count)
                if is_seat:
                    break
                current_column_index -= 1
                current_row_index -= 1

    return occupied_count, empty_count 

# looking for the upper and lower rows
# and for the items at the right and left of the current row
def solve(problem_input: List[List[str]], is_part_two: bool) -> list:
    result = []
    for row_index in range(0, len(problem_input)):
        line = []
        for column_index in range(0, len(problem_input[row_index])):
            occupied_count = 0
            empty_count = 0
            current_item: chr = problem_input[row_index][column_index]

            if current_item == ".":
                line.append(current_item)
                continue

            if is_part_two:
                occupied_count, empty_count = check_visible_seats(problem_input, occupied_count, empty_count, row_index, column_index, len(problem_input) - 1, len(problem_input[row_index]) - 1)

                if occupied_count >= 5 and current_item == "#":
                    current_item = 'L'
                elif occupied_count == 0 and current_item == 'L':
                    current_item = '#'
            else:
                # for all non corner-cases (middle columns and middle rows):
                if row_index > 0 and row_index < len(problem_input) - 1 and column_index > 0 and column_index < len(problem_input[row_index]) - 1:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index + 1], occupied_count, empty_count)

                # last row but "middle" columns
                if row_index == len(problem_input) - 1 and column_index > 0 and column_index < len(problem_input[row_index]) - 1:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index - 1], occupied_count, empty_count)

                # first row but "middle" columns
                if row_index == 0 and column_index > 0 and column_index < len(problem_input[row_index]) - 1:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index - 1], occupied_count, empty_count)

                # first column but "middle" rows
                if column_index == 0 and row_index > 0 and row_index < len(problem_input) - 1:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index + 1], occupied_count, empty_count)

                # last column but "middle" rows
                if row_index > 0 and row_index < len(problem_input) - 1 and column_index == len(problem_input[row_index]) - 1:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index - 1], occupied_count, empty_count)

                # first row and column
                if row_index == 0 and column_index == 0:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index + 1], occupied_count, empty_count)

                # last row and column
                if row_index == len(problem_input) - 1 and column_index == len(problem_input[row_index]) - 1:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index - 1], occupied_count, empty_count)

                # first row and last column
                if row_index == 0 and column_index == len(problem_input[row_index]) - 1:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index + 1][column_index - 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index - 1], occupied_count, empty_count)
                
                # last row and first column
                if row_index == len(problem_input) - 1 and column_index == 0:
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index][column_index + 1], occupied_count, empty_count)
                    occupied_count, empty_count = check_current_seat(problem_input[row_index - 1][column_index + 1], occupied_count, empty_count)

                if occupied_count >= 4 and current_item == "#":
                    current_item = 'L'
                elif occupied_count == 0 and current_item == 'L':
                    current_item = '#'

            line.append(current_item)
        result.append(line)

    return result
        
old_input = solve(problem_input, is_part_two)
while not_stabilized:
    new_input = solve(old_input, is_part_two)
    # UNCOMMENT FOR DEBUGGING GRIDS
    # print_grid(new_input)
    if old_input == new_input:
        not_stabilized = False
    else:
        old_input = new_input

for i, _ in enumerate(old_input):
    for j, _ in enumerate(old_input[i]):
        if old_input[i][j] == "#":
            ans += 1

print('The answer is: {}.'.format(ans))