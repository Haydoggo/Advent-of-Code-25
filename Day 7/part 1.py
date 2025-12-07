from util import *

input_path = "input.txt"
# input_path = "example input.txt"

with open(input_path) as file:
	grid = Grid.from_text(file.read(), Grid.FORMAT_CHARS)


beams : set[Vec2] = set()
for pos in grid.positions():
	if grid[pos] == "S":
		beams.add(pos)
		break

num_split = 0

for y in range(1, grid.height):
	new_beams : set[Vec2] = set()
	for beam_head in beams:
		if grid[beam_head] == "^":
			beam_head.y += 1
			new_beams.add(beam_head + E)
			new_beams.add(beam_head + W)
			num_split += 1
		else:
			beam_head.y += 1
			new_beams.add(beam_head)
	beams = new_beams

print(num_split)