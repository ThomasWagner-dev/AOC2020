with open('./data/AOC3.txt', 'r') as forest_file:
    forest = [str(f) for f in forest_file.read().splitlines()]
movement = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]
trees_total = []
for (x_movement, y_movement) in movement:
    line = 0
    place = 0
    trees = 0
    while line < len(forest):
        if forest[line][place] == '#':
            trees += 1
        line += y_movement
        place += x_movement
        place %= 31
    trees_total.append(trees)
print(trees_total)
