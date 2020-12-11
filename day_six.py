problem_input = []

# the problem is to collect every "yes" answer from every group
# (puzzle input) and return the total. Each answer should be counted if
# at least one person in the group answered "yes" to a question
# (marked from a through z). If a question had already been marked as 
# answered with "yes", no need to count that again

# part two is basically the same thing except it's not at least one answer
# the letter has to appear in EVERY answer as "yes".

# in this case I could separate the input into lists
# while a '\n' character is not found
# and keep reading it over and over again,
# looking for the number of answers on each letter
# using dp

answer = 0
dp = []
chars = [chr(num) for num in range(97, 123)]

def count_char_in_dp() -> int:
    total = 0
    for char in chars:
        every = True
        char_count = 0
        for item in dp:
            if char not in item:
                every = False
                break
        total += 1 if every else 0
    return total

with open('daysix_input.txt', 'r') as reader:
# with open('daysix_input_sample.txt', 'r') as reader:
    for line in reader:
        if line == '\n':
            answer += count_char_in_dp()

            # cleaning up current group
            dp = []
        else:
            dp.append(line.replace('\n', ''))



answer += count_char_in_dp()
print(answer)
