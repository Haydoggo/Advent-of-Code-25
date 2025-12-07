from util import *

input_file = "input.txt"
# input_file = "example input.txt"

class Equation:
	operands : list[int]
	operator : str

	def __init__(self):
		self.operands = list()

	def evaluate(self):
		running_value = self.operands[0]
		for operand in self.operands[1:]:
			match self.operator:
				case "+":
					running_value += operand
				case "*":
					running_value *= operand
		return running_value

grid : Grid
with open(input_file) as file:
	grid = Grid.from_text(file.read(), content_format=Grid.FORMAT_CHARS)

running_total = 0

equations : list[Equation] = []

for line in grid.content:
	print(line)

for operator_pos in [Vec2(x, grid.height-1) for x in range(grid.width)]:
	operator = grid[operator_pos]
	if operator in (" ", None):
		continue
	equation = Equation()
	equation.operator = operator
	max_width = 0
	for x in range(1, 10):
		c = grid[operator_pos + E*x]
		if c == " ":
			max_width += 1
		else:
			if c is None:
				max_width += 1
			break

	for x in range(operator_pos.x, operator_pos.x + max_width):
		operand_text = ""
		for y in range(grid.height-1):
			c : str = grid[Vec2(x,y)]
			if c.isnumeric():
				operand_text += c
		equation.operands.append(int(operand_text))
		print(operand_text)

	print(operator)
	result = equation.evaluate()
	print(f"= {result}\n")
	running_total += result

print("total: ", running_total)