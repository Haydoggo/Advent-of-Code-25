
input_path = "input.txt"
# input_path = "example input.txt"

lines : list[str]
with open(input_path) as file:
	lines = file.read().split("\n")

total_joltage = 0
for line in lines:
	max_joltage = 0
	for i, first in enumerate(line):
		for second in line[i+1:]:
			joltage = int(first + second)
			max_joltage = max(joltage, max_joltage)
	print(max_joltage)
	total_joltage += max_joltage
print(total_joltage)