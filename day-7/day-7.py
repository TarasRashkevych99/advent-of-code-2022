import math

class Directory:
    def __init__(self):
        self.parent = None
        self.children = []
        self.name = None
        self.size = 0

def calculate_sizes(current_dir):
    if len(current_dir.children) == 0:
        return current_dir.size
    else:
        sizes = []
        for child in current_dir.children:
            sizes.append(calculate_sizes(child))
        current_dir.size += sum(sizes)
        return current_dir.size

def get_total_size(current_dir):
    if len(current_dir.children) == 0:
        if current_dir.size <= 100000:
            return current_dir.size
        else:
            return 0
    else:
        sizes = []
        for child in current_dir.children:
            sizes.append(get_total_size(child))
        if current_dir.size <= 100000:
            return current_dir.size + sum(sizes)
        else:
            return sum(sizes)

def get_smallest_space_to_free(current_dir, space_still_missing):
    if len(current_dir.children) == 0:
        if current_dir.size >= space_still_missing:
            return current_dir.size
        else:
            return math.inf
    else:
        sizes = []
        for child in current_dir.children:
            sizes.append(get_smallest_space_to_free(child, space_still_missing))
        if current_dir.size >= space_still_missing:
            sizes.append(current_dir.size)
        return min(sizes)

def part_1():
    import os

    with open(os.path.join(os.path.dirname(__file__), "day-7.txt")) as f:
        input = f.read()
    
    lines = input.splitlines()

    root_dir = Directory()
    root_dir.name = "/"

    current_dir = root_dir

    for line in lines:
        tokens = line.split(' ')
        if tokens[0] == '$':
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    current_dir = current_dir.parent
                elif tokens[2] != "/":
                    current_dir = [x for x in current_dir.children if x.name == tokens[2]][0]
            elif tokens[1] == "ls":
                continue
        elif tokens[0] == "dir":
            child_dir = Directory()
            child_dir.name = tokens[1]
            child_dir.parent = current_dir
            current_dir.children.append(child_dir)
        else:
            current_dir.size += int(tokens[0])

    calculate_sizes(root_dir)
    print(get_total_size(root_dir))

def part_2():
    import os

    with open(os.path.join(os.path.dirname(__file__), "day-7.txt")) as f:
        input = f.read()
    
    lines = input.splitlines()

    root_dir = Directory()
    root_dir.name = "/"

    current_dir = root_dir

    for line in lines:
        tokens = line.split(' ')
        if tokens[0] == '$':
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    current_dir = current_dir.parent
                elif tokens[2] != "/":
                    current_dir = [x for x in current_dir.children if x.name == tokens[2]][0]
            elif tokens[1] == "ls":
                continue
        elif tokens[0] == "dir":
            child_dir = Directory()
            child_dir.name = tokens[1]
            child_dir.parent = current_dir
            current_dir.children.append(child_dir)
        else:
            current_dir.size += int(tokens[0])

    calculate_sizes(root_dir)
    unused_space = 70000000 - root_dir.size
    space_still_missing = 30000000 - unused_space
    print(get_smallest_space_to_free(root_dir, space_still_missing))

if __name__ == "__main__":
    part_1()
    part_2()