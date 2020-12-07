with open('./data/AOC1.txt', 'r') as num_file:
    numbers = [int(f) for f in num_file.readlines()]
    print(numbers)
i = 1
for num in numbers:
    for j in range(i, len(numbers)):
        m = 1
        for k in range(m, len(numbers)):
            if num + numbers[j] + numbers[k] == 2020:
                print(f'The Answers are {num}, {numbers[j]} and {numbers[k]}')
