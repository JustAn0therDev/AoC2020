problem_input = []

with open('dayone_input.txt', 'r') as reader:
    for line in reader:
        problem_input.append(int(line))

ans = 0

def solve(list_input: list) -> int:
    for i in list_input:
        for j in list_input:
            for k in list_input:
                # first part is only i + j resulting in 2020
                # second part envolves another loop
                if i + j + k == 2020:
                    return i * j * k

print(solve(problem_input))
