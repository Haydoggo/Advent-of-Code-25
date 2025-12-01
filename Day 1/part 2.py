with open("input.txt") as file:
	lines = file.readlines()

pointer = 50
count = 0
for line in lines:
	line = line.strip()

	num = int(line[1:])
	dir = 1 if line[0] == "R" else -1
	for i in range(abs(num)):
		pointer += dir
		if pointer == 100:
			pointer = 0
		if pointer == -1:
			pointer = 99
		if pointer == 0:
			count+=1
	print(line, pointer)

print(count)