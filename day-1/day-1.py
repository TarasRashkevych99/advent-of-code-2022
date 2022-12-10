import os

def part_1():
    with open(os.path.join(os.path.dirname(__file__), 'day-1.txt')) as f:
        input = f.read()

    groupsOfCalories = input.split("\n\n")

    sumsOfGroupsOfCalories = [sum([int(x) for x in group.split("\n")]) for group in groupsOfCalories]

    print(max(sumsOfGroupsOfCalories))

def part_2():
    with open(os.path.join(os.path.dirname(__file__), 'day-1.txt')) as f:
        input = f.read()

    groupsOfCalories = input.split("\n\n")

    sumsOfGroupsOfCalories = [sum([int(x) for x in group.split("\n")]) for group in groupsOfCalories]

    sumsOfGroupsOfCalories.sort()

    print(sum(sumsOfGroupsOfCalories[len(sumsOfGroupsOfCalories) - 3::]))


if __name__ == "__main__":
    part_1()
    part_2()