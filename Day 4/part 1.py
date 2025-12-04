from util import *

input_path = "input.txt"
# input_path = "example input.txt"

grid : Grid
with open(input_path) as file:
	grid = Grid.from_text(file.read(), Grid.FORMAT_CHARS)

grid2 : Grid
with open(input_path) as file:
	grid2 = Grid.from_text(file.read(), Grid.FORMAT_CHARS)


num_rolls = 0
for pos in grid.positions():
	adjacent_rolls = 0
	if grid[pos] != "@":
		continue
	for neighbour in EightDirs:
		if grid[pos + neighbour] == "@":
			adjacent_rolls+= 1
	if adjacent_rolls < 4:
		num_rolls+= 1
		grid2[pos] = "x"


# for line in grid2.content:
# 	print("".join(line))

for line in grid.content:
	print("".join(line))
print(num_rolls)