class IDRange():
	start : int
	end : int
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def contains_id(self, id_num):
		return self.start <= id_num <= self.end

input_file = "input.txt"
input_file = "example input.txt"

with open(input_file) as file:
	input_text = file.read()

id_ranges_text, ids_text = [group.split("\n") for group in input_text.split("\n\n")]

id_ranges : list[IDRange] = []

for id_range_text in id_ranges_text:
	start, end = [int(val) for val in id_range_text.split("-")]
	id_ranges.append(IDRange(start, end))

ids = [int(id_num) for id_num in ids_text]

fresh_ids = 0
for id_num in ids:
	for id_range in id_ranges:
		if id_range.contains_id(id_num):
			fresh_ids += 1
			break
