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

input_lines : list[str]
with open(input_file) as file:
	input_lines = [line.strip() for line in file.readlines()]

num_cols = len(input_lines[0].split())
equations : list[Equation] = []

operators = input_lines[-1].split()

for col in range(num_cols):
	equation = Equation()
	equation.operator = operators[col]
	equations.append(equation)


for line in input_lines[:-1]:
	operands = [int(val) for val in line.split()]
	for i, equation in enumerate(equations):
		equation.operands.append(operands[i])


grand_total = 0
for equation in equations:
	equation_value = equation.evaluate()
	print(equation_value)
	grand_total += equation_value

print(grand_total)