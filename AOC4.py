import re
with open('./data/AOC4.txt', 'r') as passport_file:
    passports_sep = []
    for elem in passport_file.read().splitlines():
        passports_sep.extend(elem.split(' '))

passports = []
temp_passport = []
for i in range(0, len(passports_sep)):
    entry = passports_sep[i]
    if entry != '':
        temp_passport.append(entry)
    else:
        passports.append(temp_passport)
        temp_passport = []
passports.append(temp_passport)

def part_one():
    valid = 0
    for passport in passports:
        if len(passport) == 7:
            cid = False
            for entry in passport:
                if entry.split(':')[0] == 'cid':
                    cid = True
            if not cid:
                valid += 1
        if len(passport) == 8:
            valid += 1
    return valid


def part_two():
    # Sanitize Input
    for passport in passports:
        for entry in passport:
            if entry.split(':')[0] == 'cid':
                passport.remove(entry)
    # Map input
    passport_maps = []
    for passport in passports:
        temp_map = {}
        for entry in passport:
            t = tuple(entry.split(':'))
            temp_map[t[0]] = t[1]
        passport_maps.append(temp_map)
    valid = 0
    for map in passport_maps:
        if len(map) == 7:
            # Validate Birth Year
            if not 1920 <= int(map['byr']) <= 2002:
                continue
            # Validate Issue Year
            if not 2010 <= int(map['iyr']) <= 2020:
                continue
            # Validate Expiration Year
            if not 2020 <= int(map['eyr']) <= 2030:
                continue
            # Validate Height
            if map['hgt'].endswith('cm'):

                if not 150 <= int(map['hgt'][0:-2]) <= 193:
                    continue
            elif map['hgt'].endswith('in'):
                if not 59 <= int(map['hgt'][0:-2]) <= 76:
                    continue
            else:
                continue
            # Validate Hair Color
            regex = r'[0-9a-f]{6}'
            if re.search(regex, map['hcl']) is None or len(map['hcl']) != 7:
                continue
            # Validate Eye Color
            if map['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                continue
            # Validate Passport ID
            if re.search(regex, map['pid']) is None or len(map['pid']) != 9:
                continue
            valid += 1
    return valid


if __name__ == '__main__':
    print(f'{part_one()} passport are valid following the rules of part one.')
    print(f'{part_two()} passport are valid following the rules of part two.')