import re
with open('./data/AOC2.txt') as data:
    passwords = [str(f).replace(':', '').replace('-', ' ').replace('\n', '') for f in data.readlines()]


def number_one():
    valid = 0
    for line in passwords:
        min, max, letter, password_full = line.split(' ')
        regex = f'[^{letter}]*'
        password = re.sub(regex, '', password_full)
        if min <= len(password) <= max:
            valid += 1
    print(valid)


def number_two():
    valid = 0
    for line in passwords:
        pos1, pos2, letter, password = line.split(' ')
        letters = password[int(pos1) - 1] + password[int(pos2) - 1]
        if letters.count(letter) == 1:
            valid += 1
    print(valid)


if __name__ == '__main__':
    number_two()