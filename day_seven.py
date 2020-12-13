import re

rules = []
bag_set = {'shiny gold'}

with open('dayseven_input.txt', 'r') as reader:
# with open('dayseven_input_sample.txt', 'r') as reader:
# with open('dayseven_input_sample_part2.txt', 'r') as reader:
    for line in reader:
        rules.append(line)

# Part One
# modifies set by reference
def part_one(bag_set: set) -> None:
    for _ in range (0, len(rules)):
        for line in rules:
            split_line = line.replace('bags', '').replace('contain', '').split('  ')
            another_bag_set = set()
            for bag in bag_set:
                if not line.startswith(bag) and bag in line:
                    another_bag_set.add(split_line[0])
            bag_set.update(another_bag_set)

# to get the solution: print(len(bag_set) - 1) | ps: ("- 1" being the shiny gold bag that does not count)

# Part Two

# Returns int receiving tuple with bag name and amount, calling the innermost bags using recursion 
def part_two(bag_name: tuple) -> int:
    count = 1 
    for line in rules:
        split_line = line.replace('bags', '').replace('contain', '').split('  ')
        if line.startswith(bag_name[0]) or bag_name[0] == split_line[0] or bag_name[0] in split_line[0]:
            regex = re.compile('[^a-zA-Z ]')
            innermost_bags = [regex.sub('', item).strip() for item in split_line[1].split(',')]

            regex = re.compile('[^0-9]')
            innermost_bag_number = [regex.sub('', item).strip() for item in split_line[1].split(',')]

            bags_and_qtd = list(zip(innermost_bags, innermost_bag_number))

            for bag in bags_and_qtd:
                if ('no other' not in bag[0] or bag[0] != 'no other') and bag[1] is not None:
                    print(bag)
                    result = part_two(bag)
                    if type(result) == int:
                        count += int(bag[1]) * result
    return count
    
# again, the count should have - 1 to exclude the shiny gold bag previously included in the list
print(part_two(('shiny gold', '1')) - 1)
