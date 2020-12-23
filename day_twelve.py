from typing import List

problem_input = []

# with open('daytwelve_input_sample.txt', 'r') as reader:
with open('daytwelve_input.txt', 'r') as reader:
    for line in reader:
        if line != '\n':
            problem_input.append(line.replace('\n', ''))

class Point:
    north: int
    south: int
    east: int
    west: int
    active_direction: str

    def __init__(self):
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0
        self.active_direction = 'east'

    def get_manhattan_distance(self) -> int:
        return self.north + self.east + self.west + self.south

    def set_active_direction(self, instruction: str, value: int) -> None:
        if instruction == 'L':
            if self.active_direction == 'north':
                if value == 90:
                    self.active_direction = 'west'
                elif value == 180:
                    self.active_direction = 'south'
                else:
                    self.active_direction = 'east'
            elif self.active_direction == 'west':
                if value == 90:
                    self.active_direction = 'south'
                elif value == 180:
                    self.active_direction = 'east'
                else:
                    self.active_direction = 'north'
            elif self.active_direction == 'south':
                if value == 90:
                    self.active_direction = 'east'
                elif value == 180:
                    self.active_direction = 'north'
                else:
                    self.active_direction = 'west'
            else:
                if value == 90:
                    self.active_direction = 'north'
                elif value == 180:
                    self.active_direction = 'west'
                else:
                    self.active_direction = 'south'
        else:
            if self.active_direction == 'north':
                if value == 90:
                    self.active_direction = 'east'
                elif value == 180:
                    self.active_direction = 'south'
                else:
                    self.active_direction = 'west'
            elif self.active_direction == 'west':
                if value == 90:
                    self.active_direction = 'north'
                elif value == 180:
                    self.active_direction = 'east'
                else:
                    self.active_direction = 'south'
            elif self.active_direction == 'south':
                if value == 90:
                    self.active_direction = 'west'
                elif value == 180:
                    self.active_direction = 'north'
                else:
                    self.active_direction = 'east'
            else:
                if value == 90:
                    self.active_direction = 'south'
                elif value == 180:
                    self.active_direction = 'west'
                else:
                    self.active_direction = 'north'

# modifies point instance by reference
def check_instruction(point: Point, instruction: str, value: int) -> None:
    if instruction == 'L' or instruction == 'R':
        point.set_active_direction(instruction, value)
    else:
        if instruction == 'N' or (instruction == 'F' and point.active_direction == 'north'):
            if value - point.south > 0:
                value -= point.south
                point.north += value
                point.south = 0
            else:
                point.south -= value
        elif instruction == 'S' or (instruction == 'F' and point.active_direction == 'south'):
            if value - point.north > 0:
                value -= point.north
                point.south += value
                point.north = 0
            else:
                point.north -= value
        elif instruction == 'E' or (instruction == 'F' and point.active_direction == 'east'):
            if value - point.west > 0:
                value -= point.west
                point.east += value
                point.west = 0
            else:
                point.west -= value
        elif instruction == 'W' or (instruction == 'F' and point.active_direction == 'west'):
            if value - point.east > 0:
                value -= point.east
                point.west += value
                point.east = 0
            else:
                point.east -= value

def solve_part_one(problem_input: List[str]) -> int:
    point: Point = Point()
    for move in problem_input:
        instruction, value = (move[0], int(move[1:]))
        check_instruction(point, instruction, value)

    return point.get_manhattan_distance()

print(solve_part_one(problem_input))