with open("input.txt") as file:
	lines = file.readlines()

pointer = 50
count = 0
for line in lines:
	line = line.strip()

	num = int(line[1:])
	if line[0] == "L":
		pointer -= num
	else:
		pointer += num

	while pointer >= 100:
		pointer -= 100
	while pointer < 0:
		pointer += 100

	if pointer == 0:
		count+=1
	print(line, pointer)

print(count)