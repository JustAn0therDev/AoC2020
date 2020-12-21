from copy import copy
from typing import List, Tuple
problem_input = []
not_stabilized = True
ans = 0

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

# looking for the upper and lower rows
# and for the items at the right and left of the current row
def solve_part_one(problem_input: List[List[str]]) -> list:
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
        
old_input = solve_part_one(problem_input)
while not_stabilized:
    new_input = solve_part_one(old_input)
    if old_input == new_input:
        not_stabilized = False
    else:
        old_input = new_input

for i, _ in enumerate(old_input):
    for j, _ in enumerate(old_input[i]):
        if old_input[i][j] == "#":
            ans += 1

print('The answer is: {}.'.format(ans))