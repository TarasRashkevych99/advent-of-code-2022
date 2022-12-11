def part_1():
    import os

    wrong_items = []

    with open(os.path.join(os.path.dirname(__file__), "day-3.txt")) as f:
        input = f.read()

    rucksacks = input.split('\n')

    for rucksack in rucksacks:
        first_compartment = set(list(rucksack[:len(rucksack) // 2]))
        second_compartment = set(list(rucksack[len(rucksack) // 2:]))

        item_in_common = first_compartment.intersection(second_compartment)

        if len(item_in_common) != 0:
            wrong_items.extend(item_in_common)

    priorities = []

    for item in wrong_items:
        if item.islower():
            priorities.append(ord(item) - ord('a') + 1)
        elif item.isupper():
            priorities.append(ord(item) - ord('A') + 26 + 1)

    print(sum(priorities))


def part_2():
    import os

    badges = []

    with open(os.path.join(os.path.dirname(__file__), "day-3.txt")) as f:
        input = f.read()

    rucksacks = input.split('\n')

    priorities = []
    counter = 0

    for rucksack in rucksacks:
        badges.append(rucksack)
        counter = counter + 1
        if counter % 3 == 0 and counter != 0:
            first_rucksack = set(list(badges[0]))
            second_rucksack = set(list(badges[1]))
            third_rucksack = set(list(badges[2]))

            item_in_common = []
            item_in_common.extend(first_rucksack.intersection(second_rucksack).intersection(third_rucksack))
            item = item_in_common.pop()
            if item.islower():
                priorities.append(ord(item) - ord('a') + 1)
            elif item.isupper():
                priorities.append(ord(item) - ord('A') + 26 + 1)
            badges.clear()
            counter = 0

    print(sum(priorities))

if __name__ == "__main__":
    part_1()
    part_2()