import os

class PartNumber:
    def __init__(self, number_start: int, number_end: int, number_value: int, line_number: int) -> None:
        self.x_start = number_start
        self.x_end = number_end
        self.y = line_number
        self.value = number_value
    
    def __repr__(self) -> str:
        return (f"Part {self.value} at {[self.x_start, self.y]}")


def find_and_output_parts(line: str, line_number):
    numbers = []
    in_number = False
    number_start = None
    number_end = None
    for i in range(len(line)):
        if line[i].isdigit():
            if not in_number:
                in_number = True
                number_start = i
        else:
            if in_number:
                in_number = False
                number_end = i
                number_value = int(line[number_start:number_end])
                numbers.append(PartNumber(number_start, number_end, number_value, line_number))
                #print(f"In line {line}, finished traversing number {number_value} between pos {number_start} and {number_end}, saved to PartNumber {numbers[-1]}")
    return numbers


def number_is_next_to_symbol(x_start: int, x_end: int, y: int, grid):
    # Should check symbols at x_start - 1, x_end + 1 and [x_start - 1: x_end + 1] for y - 1 and y + 1
    # protect x and y ranges from out of bounds:
    x_start = max(0, x_start - 1)
    x_end = min(len(grid[0]) - 1, x_end + 1)
    y_start = max(0, y - 1)
    y_end = min(y + 1, len(grid) - 1)
    for i in range(y_start, y_end + 1):
        for j in range(x_start, x_end + 1):
            char = grid[i][j]
            if not char.isdigit() and not char in '.\n':
                #print(f"In {line=}, in string slice {line[x_start:x_end]}, found symbol {char}")
                return True
    return False


with open(os.getcwd() + '/input') as f:
    grid = f.readlines()
    all_part_numbers = []
    for i in range(len(grid)):
        for part in find_and_output_parts(grid[i], i):
            all_part_numbers.append(part)
    sum = 0
    for part in all_part_numbers:
        #print(part)
        if (number_is_next_to_symbol(part.x_start, part.x_end, part.y, grid)):
            sum += part.value
    print(sum)
