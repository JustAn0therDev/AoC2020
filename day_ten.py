from typing import List, Tuple

problem_input = []
    
# with open('dayten_input_sample_1.txt', 'r') as reader:
# with open('dayten_input_sample_2.txt', 'r') as reader:
with open('dayten_input.txt', 'r') as reader:
    for line in reader:
        problem_input.append(int(line.replace('\n', '')))
    
# adding the device adapter jolting
problem_input.append(max(problem_input) + 3)

problem_input.sort()

print('Problem input: {}'.format(problem_input))

# solving the first part of the problem; same thing that has done to the part 2 of the shiny bag problem (day seven)
def solve(problem_input: List[int], index: int, diff_three_count: int, diff_one_count: int) -> Tuple[int]:
    # because we're always checking index + 1, the len(problem_input) should always be measured by two
    if index != 0 and index <= len(problem_input) - 2:
        if problem_input[index + 1] - problem_input[index] == 1:
            diff_one_count += 1
        elif problem_input[index + 1] - problem_input[index] == 3:
            diff_three_count += 1
        return solve(problem_input, index + 1, diff_three_count, diff_one_count)
    elif index == 0:
        if problem_input[index] == 1:
           diff_one_count += 1
           return solve(problem_input, index + 1, diff_three_count, diff_one_count + 1)
        elif problem_input[index] == 3:
            diff_three_count += 1
            return solve(problem_input, index + 1, diff_three_count + 1, diff_one_count)
    else:
        return diff_three_count, diff_one_count

# one for "diff_three_count" because the device difference from the biggest adapter jolting value is always true
answer = solve(problem_input, 0, 0, 0)

print('The answer is: {}'.format(answer[0] * answer[1]))

# this is going to be really cool... haha...
def solve_part_two(problem_input: List[int]):
    return len(problem_input) * len(problem_input)

print(solve_part_two(problem_input))
