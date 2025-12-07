class Vec2:
	x: int
	y: int

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __add__(self, other) -> Vec2:
		return Vec2(self.x + other.x, self.y + other.y)

	def __sub__(self, other) -> Vec2:
		return Vec2(self.x - other.x, self.y - other.y)

	def __neg__(self) -> Vec2:
		return Vec2(-self.x, -self.y)

	def __mul__(self, other):
		if type(other) == int:
			return Vec2(self.x * other, self.y * other)
		elif type(other) == Vec2:
			return Vec2(self.x * other.x, self.y * other.y)
		raise TypeError(f"invalid multiplication of Vec2 and {type(other)}")

	def __eq__(self, other: Vec2):
		return type(other) == Vec2 and self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash((self.x, self.y))

	def __repr__(self):
		return f"({self.x}|{self.y})"

	def copy(self) -> Vec2:
		return Vec2(self.x, self.y)

	def rotated(self, clockwise: bool):
		if clockwise:
			return Vec2(-self.y, self.x)
		else:
			return Vec2(self.y, self.y)

N = Vec2(0, -1)
E = Vec2(1, 0)
S = Vec2(0, 1)
W = Vec2(-1, 0)
NE = N + E
SE = S + E
SW = S + W
NW = N + W

FourDirs = [N, E, S, W]
EightDirs = FourDirs + [NE, SE, SW, NW]

class Grid:
	width: int
	height: int

	content: list[list]

	read_fail_allowed = True
	write_fail_allowed = True

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.content = []
		for i in range(height):
			self.content.append([0] * width)

	def __getitem__(self, position: Vec2):
		if not self.has(position):
			if self.read_fail_allowed:
				return None
			raise KeyError(f"position {position} is out of bounds")
		return self.content[position.y][position.x]

	def __setitem__(self, position, value):
		if not self.has(position):
			if self.write_fail_allowed:
				return
			raise KeyError(f"position {position} is out of bounds")
		self.content[position.y][position.x] = value

	def has(self, position: Vec2):
		return (0 <= position.x < len(self.content[position.y]) and
				0 <= position.y < self.height)

	def near_edge(self, position: Vec2, dist = 0):
		return position.x <= dist or position.y <= dist or position.x >= self.width - 1 - dist or position.y >= self.height - 1 - dist

	def positions(self) -> list[Vec2]:
		positions : list[Vec2] = []
		for y in range(self.height):
			for x in range(self.width):
				positions.append(Vec2(x,y))
		return positions

	def allow_read_fail(self, allow : bool = True):
		self.read_fail_allowed = allow

	def allow_write_fail(self, allow : bool = True):
		self.write_fail_allowed = allow

	FORMAT_NUMBERS = 0
	FORMAT_CHARS = 1

	@staticmethod
	def from_text(text, content_format=FORMAT_NUMBERS):
		lines = text.split("\n")

		grid = Grid(0, 0)
		grid.content.clear()

		for line in lines:
			match content_format:
				case Grid.FORMAT_NUMBERS:
					line = [int(val) for val in line]
				case Grid.FORMAT_CHARS:
					line = list(line)
			grid.width = max(grid.width, len(line))
			grid.height += 1
			grid.content.append(line)

		for line in grid.content:
			padding_amount = grid.width - len(line)

			match content_format:
				case Grid.FORMAT_NUMBERS:
					line += [0] * padding_amount
				case Grid.FORMAT_CHARS:
					line += [" "] * padding_amount
		return grid

	def copy(self) -> Grid:
		new_grid = Grid(self.width, self.height)
		new_grid.content.clear()
		for line in self.content:
			new_grid.content.append(line.copy())
		return new_grid

def get_columns(lines: list[str], seperator) -> list[list[int]]:
	num_cols = len(lines[0].split(seperator))
	cols = []
	for i in range(num_cols):
		cols.append([])

	for line in lines:
		for i, element in enumerate(line.split(seperator)):
			cols[i] = element

	return cols