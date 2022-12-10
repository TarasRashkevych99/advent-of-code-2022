import os

def part_1():
    with open(os.path.join(os.path.dirname(__file__), 'day-1.txt')) as f:
        input = f.read()

    groups_of_calories = input.split("\n\n")

    sums_of_groups_of_calories = [sum([int(x) for x in group.split("\n")]) for group in groups_of_calories]

    print(max(sums_of_groups_of_calories))

def part_2():
    with open(os.path.join(os.path.dirname(__file__), 'day-1.txt')) as f:
        input = f.read()

    groups_of_calories = input.split("\n\n")

    sums_of_groups_of_calories = [sum([int(x) for x in group.split("\n")]) for group in groups_of_calories]

    sums_of_groups_of_calories.sort()

    print(sum(sums_of_groups_of_calories[len(sums_of_groups_of_calories) - 3::]))


if __name__ == "__main__":
    part_1()
    part_2()