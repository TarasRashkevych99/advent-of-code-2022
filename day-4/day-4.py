def part_1():
    import os

    with open(os.path.join(os.path.dirname(__file__), "day-4.txt")) as f:
        input = f.read()

    pairs = input.split('\n')

    number_target_pairs = 0

    for pair in pairs:
        ranges = pair.split(',')
        range_1 = ranges[0].split('-')
        range_1 = set(range(int(range_1[0]), int(range_1[1]) + 1))
        range_2 = ranges[1].split('-')
        range_2 = set(range(int(range_2[0]), int(range_2[1]) + 1))

        if range_1.issuperset(range_2) or range_2.issuperset(range_1):
            number_target_pairs += 1
    
    print(number_target_pairs)

def part_2():
    import os

    with open(os.path.join(os.path.dirname(__file__), "day-4.txt")) as f:
        input = f.read()

    pairs = input.split('\n')

    number_target_pairs = 0

    for pair in pairs:
        ranges = pair.split(',')
        range_1 = ranges[0].split('-')
        range_1 = set(range(int(range_1[0]), int(range_1[1]) + 1))
        range_2 = ranges[1].split('-')
        range_2 = set(range(int(range_2[0]), int(range_2[1]) + 1))

        if len(range_1.intersection(range_2)) != 0:
            number_target_pairs += 1
    
    print(number_target_pairs)

if __name__ == "__main__":
    part_1()
    part_2()