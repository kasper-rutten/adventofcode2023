import os
from collections import Counter

class PartNumber:
    def __init__(self, number_start: int, number_end: int, number_value: int, line_number: int) -> None:
        self.x_start = number_start
        self.x_end = number_end
        self.y = line_number
        self.value = number_value
        self.asterisk = None
    
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


def number_is_next_to_asterisk(x_start: int, x_end: int, y: int, grid, part) -> bool:
    # Should check symbols at x_start - 1, x_end + 1 and [x_start - 1: x_end + 1] for y - 1 and y + 1
    # protect x and y ranges from out of bounds:
    x_start = max(0, x_start - 1)
    x_end = min(len(grid[0]) - 1, x_end + 1)
    y_start = max(0, y - 1)
    y_end = min(y + 1, len(grid) - 1)
    for i in range(y_start, y_end + 1):
        for j in range(x_start, x_end):
            if grid[i][j] == '*':
                #print(f"In {grid[i]=}, in string slice {grid[i][x_start:x_end]}, found asterisk, writing to {part=}")
                part.asterisk = f"{i}{j}" #easier to match strings than arrays
                return True
    return False

#def count_adjacent_numbers(x, y, parts):
#    x_start = max(0, x - 1)
#    x_end = min(len(grid[0]) - 1, x + 1)
#    y_start = max(0, y - 1)
#    y_end = min(y + 1, len(grid) - 1)
#    for xi in range(x_start, x_end):
#        for yi in range(y_start, y_end):
            


with open(os.getcwd() + '/input') as f:
    grid = f.readlines()
    all_part_numbers = []
    for i in range(len(grid)):
        for part in find_and_output_parts(grid[i], i):
            all_part_numbers.append(part)
    sum = 0
    #find asterisks, for all asterisks, verify they are adjacent to exactly 2 numbers
    #for i, line in enumerate(grid):
    #    for j, char in enumerate(line):
    #        if char == '*':
    #            count_adjacent_numbers(j,i)
    all_adjacent_parts = []
    for part in all_part_numbers:
        #print(part)
        if number_is_next_to_asterisk(part.x_start, part.x_end, part.y, grid, part):
            all_adjacent_parts.append(part)
    all_asterisks = [x.asterisk for x in all_adjacent_parts]
    print(len(all_asterisks) )
    #print(all_asterisks)
    #matches_counted = Counter(all_asterisks) # equals to list(set(words))
    #exactly_two_matches = [x for x in matches_counted if matches_counted[x] == 2 ]
    #print(f"{len(exactly_two_matches)=}, {len(all_adjacent_parts)=}")
    ##print(matches_counted[exactly_two_matches[22]])
    #sum = 0
    #for gear in exactly_two_matches:
    #    rolling_product = 1
    #    for part in all_adjacent_parts:
    #        if gear in part.asterisks:
    #            print(f"found {part} matching gear {gear}, multiplying {rolling_product=} by {part.value=}")
    #            rolling_product *= part.value
    #    sum += rolling_product
#
    #print(sum)
