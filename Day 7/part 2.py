from util import *

class Beam:
	pos : Vec2
	count : int

	def __init__(self, pos):
		self.pos = pos
		self.splits = 1


def increment_density(pos : Vec2, densities : dict[Vec2, int]):
	densities[pos] = densities.get(pos, 0) + 1

def main():
	input_path = "input.txt"
	# input_path = "example input.txt"

	with open(input_path) as file:
		grid = Grid.from_text(file.read(), Grid.FORMAT_CHARS)


	beam_density : dict[Vec2, int] = {}
	for pos in grid.positions():
		if grid[pos] == "S":
			beam_density[pos] = 1
			break

	for y in range(1, grid.height):
		new_densities : dict[Vec2, int] = {}
		for beam_head, beam_count in beam_density.items():
			if grid[beam_head] == "^":
				beam_head.y += 1
				for pos in (beam_head + E, beam_head + W):
					new_densities[pos] = new_densities.get(pos, 0) + beam_count
			else:
				beam_head.y += 1
				new_densities[beam_head] = new_densities.get(beam_head, 0) + beam_count
		beam_density = new_densities


	num_beams = 0
	for count in beam_density.values():
		num_beams += count

	print(num_beams)


main()