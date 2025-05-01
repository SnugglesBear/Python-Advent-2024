# read in puzzle input as an array of new lines
# have something scan for starting with x's. check around on same line and surrounding lines (+/0/- one index) for an m
# once you have decided on a path (diagonal, backwards, whatever) check the next position for an a and same for s after that
# maybe optimize to not check a direction if it's impossible for it to be completed (for example the top left corner shouldn't check above, left, left upward diagonal)



def read_input_lines(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]
    
def find_x(lines):
    count = 0
    for line_number, line in enumerate(lines):
        for index, char in enumerate(line):
            if char == 'X':
                count = count + find_m(lines, line_number, index)
    return count

def find_m(lines, line_number, index):
    count = 0
    char = 'M'
    clock = 'E'
    index_max = len(lines[line_number]) - 1
    if index + 3 <= index_max: 
        # room for 3 characters to the left
        clock = 'E'
        next_char = lines[line_number][index + 1]
        if next_char == char:
            if (find_a(lines, line_number, index + 1, clock)):
                count += 1
    if index - 3 >= 0:
        clock = 'W'
        previous_char = lines[line_number][index - 1]
        if previous_char == char:
            if (find_a(lines, line_number, index - 1, clock)):
                count += 1
    if line_number >= 3:
        new_line = line_number - 1
        if lines[new_line][index] == char:
            clock = 'N'
            if (find_a(lines, new_line, index, clock)):
                count += 1
        if index - 3 >= 0:
            if lines[new_line][index - 1] == char:
                clock = 'NW'
                if find_a(lines, new_line, index - 1, clock):
                    count += 1
        if index + 3 <= index_max:
            if lines[new_line][index + 1] == char:
                clock = 'NE'
                if find_a(lines, new_line, index + 1, clock):
                    count += 1
    if line_number + 3 < len(lines):
        new_line = line_number + 1
        if lines[new_line][index] == char:
            clock = 'S'
            if find_a(lines, new_line, index, clock):
                count += 1
        if index - 3 >= 0:
            if lines[new_line][index - 1] == char:
                clock = 'SW'
                if find_a(lines, new_line, index - 1, clock):
                    count += 1
        if index + 3 <= index_max:
            if lines[new_line][index + 1] == char:
                clock = 'SE'
                if find_a(lines, new_line, index + 1, clock):
                    count += 1
    return count

def find_a(lines, line_number, index, clock):
    char = 'A'
    if clock == 'E':
        if lines[line_number][index + 1] == char:
            return find_s(lines, line_number, index + 1, clock)
        else: return False
    elif clock == 'W':
        if lines[line_number][index - 1] == char:
            return find_s(lines, line_number, index - 1, clock)
        else: return False
    elif clock == 'N':
        if lines[line_number - 1][index] == char:
            return find_s(lines, line_number - 1, index, clock)
        else: return False
    elif clock == 'NE':
        if lines[line_number - 1][index + 1] == char:
            return find_s(lines, line_number - 1, index + 1, clock)
        else: return False
    elif clock == 'NW':
        if lines[line_number - 1][index - 1] == char:
            return find_s(lines, line_number - 1, index - 1, clock)
        else: return False
    elif clock == 'S':
        if lines[line_number + 1][index] == char:
            return find_s(lines, line_number + 1, index, clock)
        else: return False
    elif clock == 'SE':
        if lines[line_number + 1][index + 1] == char:
            return find_s(lines, line_number + 1, index + 1, clock)
        else: return False
    elif clock == 'SW':
        if lines[line_number + 1][index - 1] == char:
            return find_s(lines, line_number + 1, index - 1, clock)
        else: return False


def find_s(lines, line_number, index, clock):
    char = 'S'
    if clock == 'E':
        if lines[line_number][index + 1] == char:
            return True
        else: return False
    elif clock == 'W':
        if lines[line_number][index - 1] == char:
            return True
        else: return False
    elif clock == 'N':
        if lines[line_number - 1][index] == char:
            return True
        else: return False
    elif clock == 'NE':
        if lines[line_number - 1][index + 1] == char:
            return True
        else: return False
    elif clock == 'NW':
        if lines[line_number - 1][index - 1] == char:
            return True
        else: return False
    elif clock == 'S':
        if lines[line_number + 1][index] == char:
            return True
        else: return False
    elif clock == 'SE':
        if lines[line_number + 1][index + 1] == char:
            return True
        else: return False
    elif clock == 'SW':
        if lines[line_number + 1][index - 1] == char:
            return True
        else: return False

def find_a_cross(lines):
    count = 0
    for line_number, line in enumerate(lines):
        for index, char in enumerate(line):
            if char == 'A':
                count = count + find_cross(lines, line_number, index)
    return count

def find_cross(lines, line_number, index):
    diagonal_one = False
    diagonal_two = False

    # check bounds
    if line_number > 0 and line_number + 1 < len(lines) and index > 0 and index + 1 < len(lines[line_number]):
        northwest = lines[line_number - 1][index - 1]
        northeast = lines[line_number - 1][index + 1]
        southwest = lines[line_number + 1][index - 1]
        southeast = lines[line_number + 1][index + 1]
        # check diagonal 1
        if (northwest == 'M' and southeast == 'S') or (northwest == 'S' and southeast == 'M'):
            diagonal_one = True
        # check diagonal 2
        if (northeast == 'M' and southwest == 'S') or (northeast == 'S' and southwest == 'M'):
            diagonal_two = True

    if (diagonal_one and diagonal_two):
        return 1
    else:
        return 0

def main():
    lines = read_input_lines("Python-Advent-2024/Day 4/input.txt")
    print(find_x(lines))

    print (find_a_cross(lines))

if __name__ == "__main__":
    main()