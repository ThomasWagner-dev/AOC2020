with open('./data/AOC5.txt', 'r') as passport_file:
    seats = [str(f) for f in passport_file.read().splitlines()]


def up_down(instruction: str, number_list):
    lower, upper = split_list(number_list)
    if instruction == 'F' or instruction == 'L':
        return lower
    elif instruction == 'B' or instruction == 'R':
        return upper


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def get_seat(input_string: str):
    row_list = list(range(0, 128))
    column_list = list(range(0, 8))
    for letter in input_string:
        if letter in {'F', 'B'}:
            row_list = up_down(letter, row_list)
        elif letter in {'L', 'R'}:
            column_list = up_down(letter, column_list)
        else:
            print(f'{input_string} is not a recognised instruction for function up_down!')
    return row_list[0], column_list[0]


def part_one():
    highest = 0
    for instruction in seats:
        seat = get_seat(instruction)
        id = seat[0] * 8 + seat[1]
        if id > highest:
            highest = id
    print(highest)


def part_two():
    possible_seats = []
    for i in range(0, 128):
        possible_seats.append(list(range(0, 8)))

    for instruction in seats:
        seat = get_seat(instruction)
        possible_seats[seat[0]].remove(seat[1])
    for i in range(0, 128):
        temp = possible_seats[i]
        if len(temp) == 1 and len(possible_seats[i - 1]) == 0 and len(possible_seats[i + 1]) == 0:
            print(i, temp[0])


if __name__ == '__main__':
    part_two()