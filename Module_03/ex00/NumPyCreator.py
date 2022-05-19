import numpy

class NumPyCreator:
	def __init__(self):
		pass

	def	from_lst(self, lst):
		try:
			if isinstance(lst, list)
				np = numpu.array(lst)
		except:
			raise TypeError("Incorrect Type")
		return np

	def	from_tuple(self, tpl):
		try:
			if isinstance(tpl, tuple)
				np = numpu.array(tpl)
		except:
			raise TypeError("Incorrect Type")
		return np

	def	from_iterable(self, itr):
		try:
			if hasattr(itr, "__iter__")
				np = numpu.array(iter)
		except:
			raise TypeError("Incorrect Type")
		return np

		return numpy.array(itr)

	def	from_shape(self, shape, value):
		return numpy.array(shape, value)

	def	random(self, shape):
		return numpy.array(shaape)

	def	identity(self, n):
		return numpy.array(n)

npc = NumPyCreator()
npc.from_list([[1,2,3],[6,3,4]])
npc.from_list([[1,2,3],[6,4]])
npc.from_list([[1,2,3],[’a’,’b’,’c’],[6,4,7]])
npc.from_list(((1,2),(3,4)))
npc.from_tuple(("a","b","c"))
npc.from_tuple([[1,2,3],[6,3,4]])
npc.from_iterable(range(5))
shape=(3,5)
npc.from_shape(shape)
npc.random(shape)
npc.identity(4)
