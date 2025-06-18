# Part 1
# make some kind of class where each number can point to its following numbers
# read the input and place the rules in the class
# read in the corrections into an array
# check each correction line by following the linked list to make sure there are no problems
# if the correction line is true, you can divide the index by 2 to get the middle, else disregard or 0
# add up the middle numbers that are correct

class Node:
    def __init__(self, data):
        self.data = data
        self.next_nodes = []
        
    def add_link(self, node):
        self.next_nodes.append(node)

    def __repr__(self):
        links = ', '.join(str(n.data) for n in self.next_nodes)
        return f"{self.data} -> [{links}]"

def read_input_lines(filename):
    with open(filename, "r") as file:
        return(file.read().splitlines())
    
def create_nodes(link_lines):
    node_map = {}

    for line in link_lines:
        src_val, dst_val = map(int, line.strip().split('|'))

        # Ensure both nodes exist
        if src_val not in node_map:
            node_map[src_val] = Node(src_val)
        if dst_val not in node_map:
            node_map[dst_val] = Node(dst_val)

        # Link source to destination
        node_map[src_val].add_link(node_map[dst_val])

    return node_map

def simplify_instructions(updates):
    simplified = [list(map(int, item.split(','))) for item in updates]
    return simplified

def check_instructions(page_rules, updates):
    count = 0
    for line in updates:
        count = count + check_line(line, page_rules)

    return count


def check_line(line, page_rules):
    count = 0

    for index in line:
        if index > 0:
            try: 
                node = page_rules(line[index])

    

def main():
    lines = read_input_lines("Python-Advent-2024/Day 5/input.txt")

    divider = lines.index('')
    rules = lines[:divider]
    updates = lines[divider + 1:]
    updates = simplify_instructions(updates)

    page_rules = create_nodes(rules)

    for node in page_rules.values():
        print(node)

if __name__ == "__main__":
    main()