rules = []
bag_set = {'shiny gold'}

with open('dayseven_input.txt', 'r') as reader:
# with open('dayseven_input_sample.txt', 'r') as reader:
    for line in reader:
        rules.append(line)

for _ in range (0, len(rules)):
    for line in rules:
        split_line = line.replace('bags', '').replace('contain', '').split('  ')
        another_bag_set = set()
        for bag in bag_set:
            if not line.startswith(bag) and bag in line:
                another_bag_set.add(split_line[0])
        bag_set.update(another_bag_set)

# the solution here should be len(bag_set) - 1 ("-1" being the shiny gold bag that is not relevant)
print(len(bag_set) - 1)
