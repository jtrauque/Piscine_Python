import sys
sys.tracebacklimit = 0

class Vector:
	def __init__(self, args):
		if isinstance(args, int):
			self.value = []
			if args > 0:
				for i in range(0, args):
					self.value.append(float(i))
			else:
				raise ValueError('Negative value')
		elif isinstance(args, tuple) and len(args) == 2:
			self.value = []
			if args[0] > args[1]:
				raise ValueError('Incorrect range')
			for i in range(args[0], args[1]):
				self.value.append(float(i))
		elif isinstance(args, list):
			if isinstance(args[0], list):
				for i in args:
					for j in i:
						if not isinstance(j, float):
							raise ValueError('The list has to contain floats')
			else:
				for i in args:
					if not isinstance(i, float):
						raise ValueError('The list has to contain floats')
			self.value = args
		else:
			raise ValueError('Not the right type of arguments')


v1 = Vector(3)
v2 = Vector((-10, 15))
v3 = Vector([0.0, 1.0, 2.0, 3.0])
v4 = Vector([[0.0], [1.0], [2.0], [3.0]])
v5 = Vector((1, -3))
for i in v1.value:
	print(i)
for i in v2.value:
	print(i)
for i in v3.value:
	print(i)
for i in v4.value:
	print(i)
