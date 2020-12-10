problem_input = []

# with open('dayfive_input_sample.txt', 'r') as reader:
with open('dayfive_input.txt', 'r') as reader:
    for line in reader:
        problem_input.append(line)

# solving first part: Find the highest seat id 

highest_seat_id: int = 0
lowest_seat_id: int = 0
total: int = 0

def get_binary_eval(bp: str) -> int:
    seat_id: str = '' 
    for char in bp:
        if char == 'B' or char == 'R':
            seat_id += '1'
        elif char == 'F' or char == 'L':
            seat_id += '0'

    return int(seat_id, 2)

converted = [get_binary_eval(bp) for bp in problem_input]

highest_seat_id = max(converted)
lowest_seat_id = min(converted)

print(highest_seat_id)

# solving second part: subtracting factor of both halves from the sum of all numbers

highest_seat_id = int(highest_seat_id)
lowest_seat_id = int(lowest_seat_id)
result = highest_seat_id * (highest_seat_id + 1) / 2 - (lowest_seat_id - 1) * (lowest_seat_id) / 2
print(result - total)
