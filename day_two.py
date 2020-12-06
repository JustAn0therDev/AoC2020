problem_input = []

with open('daytwo_input.txt', 'r') as reader:
    for line in reader:
        problem_input.append(line.strip().replace('\n', ''))

valid_password_count = 0

# first part, min and max determine the amount of occurrences of the desired character.
# second part only one of the "min" and "max" values must appear in an 1-based index of the input list
for line in problem_input:
    line = line.strip()
    occurrences_in_password = []
    inputs = line.split(':')
    first_part_of_input = inputs[0].split('-')
    min_occurrences = int(first_part_of_input[0])
    max_occurrences = int(first_part_of_input[-1][0:-1].strip())
    letter = first_part_of_input[1][-1]

    second_part_of_input = inputs[1].strip()

    for index, part in enumerate(second_part_of_input):
        if part is letter:
            occurrences_in_password.append(index + 1)

    if min_occurrences in occurrences_in_password and max_occurrences not in occurrences_in_password or min_occurrences not in occurrences_in_password and max_occurrences in occurrences_in_password:
        valid_password_count += 1

print(valid_password_count)
