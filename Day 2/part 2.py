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
	total_span += span
print("total span: ", total_span)


invalid_sum = 0
invalid_ids = set()

for pair in pairs:
	first, second = [int(num) for num in pair.split("-")]
	span = second - first
	for num in range(first, second + 1):
		text_num = str(num)
		size = len(text_num)
		for chunk_size in range(1, size//2+1):
			if (size % chunk_size) > 0:
				continue

			last_chunk = None
			for i in range(size//chunk_size):
				chunk = text_num[i*chunk_size:i*chunk_size+chunk_size]
				if last_chunk != None and chunk != last_chunk:
					break
				last_chunk = chunk
			else:
				if num not in invalid_ids:
					invalid_ids.add(num)
					print(num)
					invalid_sum += num

print(invalid_sum)
