# A for Rock
# B for Paper
# C for Scissors

# X for Rock
# Y for Paper
# Z for Scissors

# X means you need to lose, 
# Y means you need to end the round in a draw
# Z means you need to win


def part_1():
    import os

    shape_scors = {'X': 1, 'Y': 2, 'Z': 3}

    strategies = {
        "A Y": 6, 
        "B Z": 6, 
        "C X": 6,
        "A X": 3, 
        "B Y": 3, 
        "C Z": 3,
        "A Z": 0, 
        "B X": 0, 
        "C Y": 0
    }

    with open(os.path.join(os.path.dirname(__file__), "day-2.txt")) as f:
        input = f.read()

    rounds = input.split('\n')

    total_score = sum([strategies[round] + shape_scors[round.split(' ')[1]] for round in rounds])

    print(total_score)

def part_2():
    import os

    shape_scors = {'X': 1, 'Y': 2, 'Z': 3}

    strategies = {
        "A Y": 3, 
        "B Z": 6, 
        "C X": 0,
        "A X": 0, 
        "B Y": 3, 
        "C Z": 6,
        "A Z": 6, 
        "B X": 0, 
        "C Y": 3
    }

    shapes_to_choose = {
        "A Y": 'X', 
        "B Z": 'Z', 
        "C X": 'Y',
        "A X": 'Z', 
        "B Y": 'Y', 
        "C Z": 'X',
        "A Z": 'Y', 
        "B X": 'X', 
        "C Y": 'Z'
    }

    with open(os.path.join(os.path.dirname(__file__), "day-2.txt")) as f:
        input = f.read()

    rounds = input.split('\n')

    total_score = sum([strategies[round] + shape_scors[shapes_to_choose[round]] for round in rounds])

    print(total_score)

if __name__ == "__main__":
    part_1()
    part_2()