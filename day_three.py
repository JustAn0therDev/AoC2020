problem_input = ''

# testing with the input shown in the first part of the problem
# with open('daythree_input_sample.txt', 'r') as reader:
with open('daythree_input.txt', 'r') as reader:
    for line in reader:
        problem_input += line

tree_count = 0
index_count = 0
steps_taken = 0
reset_index = False

def get_substring_index(input_list) -> int:
    try:
        return input_list.index('\n')
    except:
        return -1


# credits to ThePrimagen for showing this awesome and efficient solution 
# with recursion
def solve(sequence: str, index: int = 0) -> int:
    current_endline_index = get_substring_index(sequence)
    max_index = current_endline_index if current_endline_index != -1 else len(sequence)
    tree_count = 1 if sequence[index % max_index] == "#" else 0

    if get_substring_index(sequence) == -1:
        return tree_count

    return tree_count + solve(sequence[max_index+1:], index + 3)

print(solve(problem_input))
