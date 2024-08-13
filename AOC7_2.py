import re

# Step 1: Parse the input file
container_dict = {}
with open('./data/AOC7.txt', 'r') as answer_file:
    for elem in answer_file.read().splitlines():
        parts = elem.split(' ')
        name = parts[0] + ' ' + parts[1]
        content = []
        if 'no other bags' not in elem:
            contained_bags = re.findall(r'(\d+) (\w+ \w+)', elem)
            for count, bag in contained_bags:
                content.append((int(count), bag))
        container_dict[name] = content


def count_total_bags(bag_type):
    total = 0
    for count, inner_bag in container_dict[bag_type]:
        total += count + count * count_total_bags(inner_bag)
    return total


def part_two():
    total_bags = count_total_bags('shiny gold')
    print(total_bags)


if __name__ == '__main__':
    part_two()
