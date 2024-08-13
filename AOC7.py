container_dict = {}
with open('./data/AOC7.txt', 'r') as answer_file:
    for elem in answer_file.read().splitlines():
        parts = elem.split(' ')
        name = parts[0] + ' ' + parts[1]
        content = []
        for i in range(4, len(parts), 4):
            content.append(parts[i] + ' ' + parts[i + 1] + ' ' + parts[i + 2])
        container_dict[name] = content


def part_one():
    counter = 0
    for key in container_dict.keys():
        found = False
        bags = set()
        for bag in container_dict[key]:
            bags.add(bag)
        while bags:
            for bag in bags:
                if bag.endswith('shiny gold'):
                    found = True
                    counter += 1
                    bags = set()
                    break
            if not found:
                temp = []
                for bag in bags:
                    if (bag.split(' ')[1] + ' ' + bag.split(' ')[2]) in container_dict.keys():
                        for inner_bag in container_dict[(bag.split(' ')[1] + ' ' + bag.split(' ')[2])]:
                            temp.append(inner_bag)
                bags = set()
                for bag in temp:
                    bags.add(bag)
    print(counter)


def part_two():
    counter = 0
    shiny = container_dict['shiny gold']
    bags = []
    for bag in shiny:
        bags.append(bag)


if __name__ == '__main__':
    part_one()
