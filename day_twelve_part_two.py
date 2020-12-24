from typing import List

problem_input = []

# with open('daytwelve_input_sample.txt', 'r') as reader:
with open('daytwelve_input.txt', 'r') as reader:
    for line in reader:
        problem_input.append(line.replace('\n', ''))

class Point:
    north: int
    south: int
    east: int
    west: int

    def __init__(self):
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0

    def change_point(self, value: int, point: any) -> None:
        if point.north != 0:
            self.north += point.north * value

        if point.south != 0:
            self.south += point.south * value
        
        if point.east != 0:
            self.east += point.east * value

        if point.west != 0:
            self.west += point.west * value

    def get_manhattan_distance(self) -> int:
        return abs(self.north - self.south) + abs(self.east - self.west)

class Waypoint(Point):
    def __init__(self):
        self.north = 1
        self.south = 0
        self.east = 10
        self.west = 0

    def move_waypoint(self, instruction: str,value: int) -> None:
        if instruction == 'N':
            self.north += value
        elif instruction == 'S':
            self.south += value
        elif instruction == 'E':
            self.east += value
        else:
            self.west += value

    def rotate_waypoint(self, instruction: str, value: int) -> None:
        current_north = self.north
        current_south = self.south
        current_east = self.east
        current_west = self.west

        if instruction == 'L':
            if value == 90:
                self.north = current_east 
                self.east = current_south 
                self.south = current_west 
                self.west = current_north 
            elif value == 180:
                self.north = current_south 
                self.east = current_west 
                self.south = current_north 
                self.west = current_east 
            else:
                self.north = current_west
                self.east = current_north
                self.south = current_east
                self.west = current_south
        else:
            if value == 90:
                self.north = current_west 
                self.east = current_north 
                self.south = current_east 
                self.west = current_south 
            elif value == 180:
                self.north = current_south 
                self.east = current_west
                self.south = current_north
                self.west = current_east
            else:
                self.north = current_east
                self.east = current_south
                self.south = current_west
                self.west = current_north

def solve(problem_input: List[str]) -> int:
    ship_point: Point = Point()
    waypoint: Waypoint = Waypoint()

    for movement in problem_input:
        instruction, value = (movement[0], int(movement[1:]))
        if instruction == 'F':
            ship_point.change_point(value, waypoint)
        elif instruction in ['N','S','E','W']:
            waypoint.move_waypoint(instruction, value)
        else:
            waypoint.rotate_waypoint(instruction, value)

    return ship_point.get_manhattan_distance()

print(solve(problem_input))