problem_input = ''

# testing with the input shown in the first part of the problem
# with open('daythree_input_sample.txt', 'r') as reader:
with open('daythree_input.txt', 'r') as reader:
    for line in reader:
        problem_input += line

def get_substring_index(input_list) -> int:
    try:
        return input_list.index('\n')
    except:
        return -1


# credits to ThePrimagen for showing this awesome and efficient solution 
# using recursion

def solve_original(sequence: str, index: int = 0) -> int:
    current_endline_index = get_substring_index(sequence)
    max_index = current_endline_index if current_endline_index != -1 else len(sequence)
    tree_count = 1 if sequence[index % max_index] == "#" else 0

    if get_substring_index(sequence) == -1:
        return tree_count

    return tree_count + solve_original(sequence[max_index+1:],index+3)

def solve_right_one_down_one(sequence: str, index: int = 0) -> int:
    current_endline_index = get_substring_index(sequence)
    max_index = current_endline_index if current_endline_index != -1 else len(sequence)
    tree_count = 1 if sequence[index % max_index] == "#" else 0

    if get_substring_index(sequence) == -1:
        return tree_count

    return tree_count + solve_right_one_down_one(sequence[max_index+1:],index+1)

def solve_right_five_down_one(sequence: str, index: int = 0) -> int:
    current_endline_index = get_substring_index(sequence)
    max_index = current_endline_index if current_endline_index != -1 else len(sequence)
    tree_count = 1 if sequence[index % max_index] == "#" else 0

    if get_substring_index(sequence) == -1:
        return tree_count

    return tree_count + solve_right_five_down_one(sequence[max_index+1:],index+5)

def solve_right_seven_down_one(sequence: str, index: int = 0) -> int:
    current_endline_index = get_substring_index(sequence)
    max_index = current_endline_index if current_endline_index != -1 else len(sequence)
    tree_count = 1 if sequence[index % max_index] == "#" else 0

    if get_substring_index(sequence) == -1:
        return tree_count

    return tree_count + solve_right_seven_down_one(sequence[max_index+1:],index+7)

def solve_right_one_down_two(sequence: str, index: int = 0) -> int:
    current_endline_index = get_substring_index(sequence)
    max_index = current_endline_index if current_endline_index != -1 else len(sequence)
    tree_count = 1 if sequence[index % max_index] == "#" else 0

    if get_substring_index(sequence) == -1:
        return tree_count

    return tree_count + solve_right_one_down_two(sequence[(max_index*2)+2:],index+1)


print('DEBUG')
print('Should result in 7 for sample. Real should result in: 259. Actual result: {}'.format(solve_original(problem_input)))
print('Should result in 2. Actual result: {}'.format(solve_right_one_down_one(problem_input)))
print('Should result in 3. Actual result: {}'.format(solve_right_five_down_one(problem_input)))
print('Should result in 4. Actual result: {}'.format(solve_right_seven_down_one(problem_input)))
print('Should result in 2. Actual result: {}'.format(solve_right_one_down_two(problem_input)))


""" print('Should result in 336. Actual result: {}'.format(solve_original(problem_input) * 
      solve_right_one_down_one(problem_input) * 
      solve_right_five_down_one(problem_input) * 
      solve_right_seven_down_one(problem_input) * 
      (solve_right_one_down_two(problem_input)//2)))
"""
print('Result: {}'.format(solve_original(problem_input) * 
      solve_right_one_down_one(problem_input) * 
      solve_right_five_down_one(problem_input) * 
      solve_right_seven_down_one(problem_input) * 
      solve_right_one_down_two(problem_input)))
