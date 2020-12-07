with open('./data/AOC6.txt', 'r') as answer_file:
    group_answers = []
    temp = ''
    group_sizes = []
    group_temp = 0
    for elem in answer_file.read().splitlines():
        if elem != '':
            temp += elem
            group_temp += 1
        else:
            group_answers.append(temp)
            group_sizes.append(group_temp)
            group_temp = 0
            temp = ''
    group_answers.append(temp)
    group_sizes.append(group_temp)

group_answers_unique = []
for answers in group_answers:
    group_answers_unique.append(''.join(set(answers)))

def part_one():
    yes = 0
    for group_answer_unique in group_answers_unique:
        yes += len(group_answer_unique)
    print(yes)


def part_two():
    all_yes = 0
    for i in range(0, len(group_answers)):
        for char in group_answers_unique[i]:
            if group_answers[i].count(char) == group_sizes[i]:
                all_yes += 1
    print(all_yes)


if __name__ == '__main__':
    part_two()




