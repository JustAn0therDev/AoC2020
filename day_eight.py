problem_input = []
acc = 0
part_two = True

#with open('dayeight_input_sample.txt', 'r') as reader:
with open('dayeight_input.txt', 'r') as reader:
    for line in reader:
        if line != '\n':
            problem_input.append(line.replace('\n', ''))

# to solve the problem:
# nop, acc and jmp are valid instructions in the boot loader of the mini-game
# the values at the end of each instruction will say what should be done next.
# to solve the problem as a whole, we need to keep a state of the already processed instructions
# and if the boot loader comes back to an old instruction, we stop it.

def has_key(key: any, obj: dict) -> bool:
    try:
        obj[key]
        return True
    except:
        return False

def deep_copy_and_swap_instructions(index_arg: int, full_instruction: str, to_copy: list) -> list:
    return_value = []
    for index, line in enumerate(to_copy):
        instruction = ''
        if index == index_arg:
            return_value.append(full_instruction)
            instruction = full_instruction
        else:
            return_value.append(line)
            instruction = line
    return return_value

def part_one(problem_input: list, ran_instructions: dict) -> tuple: 
    acc = 0
    index = 0
    loops = False
    last = False
    for _ in range(0, len(problem_input)):
        if index == len(problem_input) - 1:
            last = True
        
        if index not in ran_instructions: 
           ran_instructions[index] = problem_input[index]
           instructions = problem_input[index].split(' ')
           value = int(instructions[1])

           if instructions[0] == 'acc':
               acc += value
               index += 1
           elif instructions[0] == 'jmp':
               index += value
           elif instructions[0] == 'nop':
               index += 1

           if last:
               break
        else:
            loops = True
            break

    return acc, loops

acc, _ = part_one(problem_input, dict())

# brute force:
# iterate and find a nop or jmp instruction;
# change it and iterate through it
# if didn't loop, great.
# else, go to the next one, change the instructions and run again

if part_two:
    for index, line in enumerate(problem_input):
        inner_acc = 0
        loops: bool = True
        modified_problem_input = []

        instructions = line.split(' ')
        value = int(instructions[1])

        if value == 0:
            continue

        if 'jmp' in instructions[0]:
            modified_problem_input = deep_copy_and_swap_instructions(index, 'nop {}'.format(value), problem_input)
            inner_acc, loops = part_one(modified_problem_input, dict())
        elif 'nop' in instructions[0]:
            modified_problem_input = deep_copy_and_swap_instructions(index, 'jmp {}'.format(value), problem_input)
            inner_acc, loops = part_one(modified_problem_input, dict())
        else:
            continue

        print(instructions[0], instructions[1])
        print(modified_problem_input)

        if not loops:
            print(inner_acc)
            break
