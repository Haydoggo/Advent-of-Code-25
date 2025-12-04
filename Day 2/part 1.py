from util import *

input_path = "input.txt"
# input_path = "example input.txt"

lines : list[str]
grid : Grid


input_text : str
with open(input_path) as file:
	input_text = file.read()

pairs = input_text.split(",")
total_span = 0
for pair in pairs:
	first, second = [int(num) for num in pair.split("-")]
	span = second - first
	print(span)
	total_span += span


invalid_sum = 0
for pair in pairs:
	first, second = [int(num) for num in pair.split("-")]
	span = second - first
	for num in range(first, second + 1):
		text_num = str(num)
		size = len(text_num)
		if (size % 2) == 1:
			continue
		if text_num[:size//2] == text_num[size//2:]:
			invalid_sum += num

print(invalid_sum)
