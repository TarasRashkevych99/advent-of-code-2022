def part_1():
    import os

    with open(os.path.join(os.path.dirname(__file__), "day-6.txt")) as f:
        input = f.read()

    number_of_read_chars = 0
    last_four_chars = []

    for char in input:
        number_of_read_chars += 1
        last_four_chars.append(char)
        if len(last_four_chars) == 4:
            if len(last_four_chars) == len(set(last_four_chars)):
                print(number_of_read_chars)
                break
            last_four_chars.pop(0)

def part_2():
    import os

    with open(os.path.join(os.path.dirname(__file__), "day-6.txt")) as f:
        input = f.read()

    number_of_read_chars = 0
    last_four_chars = []

    for char in input:
        number_of_read_chars += 1
        last_four_chars.append(char)
        if len(last_four_chars) == 14:
            if len(last_four_chars) == len(set(last_four_chars)):
                print(number_of_read_chars)
                break
            last_four_chars.pop(0)        

if __name__ == "__main__":
    part_1()
    part_2()