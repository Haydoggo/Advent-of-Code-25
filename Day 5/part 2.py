class IDRange:
	start : int
	end : int
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def contains_id(self, id_num):
		return self.start <= id_num <= self.end

	def size(self):
		return self.end - self.start + 1

	def try_union(self, other_range : IDRange) -> IDRange|None:
		new_range = IDRange(min(self.start, other_range.start), max(self.end, other_range.end))
		if new_range.size() <= self.size() + other_range.size():
			return new_range
		else:
			return None

	def __repr__(self):
		return f"({self.start} - {self.end})"


def main():
	input_file = "input.txt"
	# input_file = "example input.txt"

	with open(input_file) as file:
		input_text = file.read()

	id_ranges_text, ids_text = [group.split("\n") for group in input_text.split("\n\n")]

	id_ranges : list[IDRange] = []

	for id_range_text in id_ranges_text:
		start, end = [int(val) for val in id_range_text.split("-")]
		id_ranges.append(IDRange(start, end))

	while True:
		new_id_ranges : list[IDRange] = []
		unionised_ranges : set[IDRange] = set()

		for i, id_range_1 in enumerate(id_ranges):
			if id_range_1 in unionised_ranges:
				continue
			for id_range_2 in id_ranges[i+1:]:
				if id_range_2 in unionised_ranges:
					continue
				union = id_range_1.try_union(id_range_2)
				if union is not None:
					new_id_ranges.append(union)
					unionised_ranges.add(id_range_1)
					unionised_ranges.add(id_range_2)
					break
			else: #failed to union with any other ranges
				new_id_ranges.append(id_range_1)

		if len(unionised_ranges) == 0:
			break

		id_ranges = new_id_ranges


	num_fresh_ids = 0
	for id_range in new_id_ranges:
		num_fresh_ids += id_range.size()

	print(num_fresh_ids)

main()