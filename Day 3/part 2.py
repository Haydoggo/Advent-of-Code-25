
input_path = "input.txt"
# input_path = "example input.txt"

lines : list[str]
with open(input_path) as file:
	lines = file.read().split("\n")


bank_size = 12
total_joltage = 0
for line in lines:
	running_joltage = ""
	for i in range(bank_size):
		biggest_num = -1
		biggest_num_index = 0
		last_available_index = len(line)-(bank_size-i-1)
		available_numbers = [int(c) for c in line[:last_available_index]]
		print(available_numbers)
		for j, num in enumerate(available_numbers):
			if num > biggest_num:
				biggest_num = num
				biggest_num_index = j
		running_joltage += str(biggest_num)
		line = line[biggest_num_index + 1:]
	max_joltage = int(running_joltage)
	print(max_joltage)
	total_joltage += max_joltage
print(total_joltage)

