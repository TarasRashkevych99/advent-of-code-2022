def part_1():
    import os

    with open(os.path.join(os.path.dirname(__file__), "day-5.txt")) as f:
        input = f.read()

    drawing_and_procedure = input.split('\n\n')

    drawing = drawing_and_procedure[0].split('\n')
    number_of_stacks = len(drawing[len(drawing) - 1].replace(' ', ''))

    stacks = [[] for _ in range(number_of_stacks)]
    drawing = drawing[:len(drawing) - 1]

    for line in drawing:
        line = line.replace(' ', '')
        line = line.replace('[', '')
        line = line.replace(']', '')
        crates = list(line)
        for i in range(len(stacks)):
            if crates[i] != '_':
                stacks[i].append(crates[i])

    stacks = [stack[::-1] for stack in stacks]

    procedure = drawing_and_procedure[1].split('\n')

    for step in procedure:
        step = step.split(' ')
        step.remove('move')
        step.remove('from')
        step.remove('to')
        (number_of_crates, from_stack, to_stack) = step
        number_of_crates = int(number_of_crates)
        from_stack = int(from_stack) - 1
        to_stack = int(to_stack) - 1
        stacks[to_stack] = stacks[to_stack] + stacks[from_stack][len(stacks[from_stack]) - number_of_crates:][::-1]
        stacks[from_stack] = stacks[from_stack][:len(stacks[from_stack]) - number_of_crates]

    print("".join([stack[len(stack) - 1] for stack in stacks]))

def part_2():
    import os

    with open(os.path.join(os.path.dirname(__file__), "day-5.txt")) as f:
        input = f.read()

    drawing_and_procedure = input.split('\n\n')

    drawing = drawing_and_procedure[0].split('\n')
    number_of_stacks = len(drawing[len(drawing) - 1].replace(' ', ''))

    stacks = [[] for _ in range(number_of_stacks)]
    drawing = drawing[:len(drawing) - 1]

    for line in drawing:
        line = line.replace(' ', '')
        line = line.replace('[', '')
        line = line.replace(']', '')
        crates = list(line)
        for i in range(len(stacks)):
            if crates[i] != '_':
                stacks[i].append(crates[i])

    stacks = [stack[::-1] for stack in stacks]

    procedure = drawing_and_procedure[1].split('\n')

    for step in procedure:
        step = step.split(' ')
        step.remove('move')
        step.remove('from')
        step.remove('to')
        (number_of_crates, from_stack, to_stack) = step
        number_of_crates = int(number_of_crates)
        from_stack = int(from_stack) - 1
        to_stack = int(to_stack) - 1
        stacks[to_stack] = stacks[to_stack] + stacks[from_stack][len(stacks[from_stack]) - number_of_crates:]
        stacks[from_stack] = stacks[from_stack][:len(stacks[from_stack]) - number_of_crates]

    print("".join([stack[len(stack) - 1] for stack in stacks]))

if __name__ == "__main__":
    part_1()
    part_2()