problem_input = []
count = 0
ans = 0
index = 0
preamble_limit = 0

# filename = 'daynine_input_sample.txt'
filename = 'daynine_input.txt'

if 'sample' in filename:
    preamble_limit = 5
else:
    preamble_limit = 25

with open(filename, 'r') as reader:
    for line in reader:
        problem_input.append(int(line.replace('\n', '')))
        count += 1

def solve(preamble_limit: int) -> int:
    for index, main_number in enumerate(problem_input):
        if index >= preamble_limit:
            valid = False
            preamble_indexes = list(reversed(range(index - preamble_limit, index)))
            for first_index in preamble_indexes:
                for second_index in preamble_indexes:
                    if problem_input[first_index] + problem_input[second_index] == main_number and problem_input[first_index] != problem_input[second_index]:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                return main_number

invalid_number = solve(preamble_limit)
print('The answer is: {}'.format(invalid_number))

# BRUTE FORCING AGAIN:
# Loop through the whole list
# For each number, sum again every number after it and check if the value is equal to the previous invalid_number variable
# If it's not, discard that number and keep looping until the sum list is found
# Return min(list) + max(list) when found

def solve_part_two(invalid_number: int) -> int:
    continguous_numbers = []
    for index, main_number in enumerate(problem_input):
        continguous_numbers.append(main_number)
        for outer_index, number in enumerate(problem_input):
            if index >= outer_index:
                continue

            continguous_numbers.append(number)
            
            if sum(continguous_numbers) == invalid_number:
                return min(continguous_numbers) + max(continguous_numbers)
            elif sum(continguous_numbers) >= invalid_number:
                continguous_numbers = []
                break
            

print('The answer for the second part is: {}'.format(solve_part_two(invalid_number)))