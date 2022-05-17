
def	ft_map(function_to_apply, iterable):
	try:
		for i in iterable:
			yield function_to_apply(i)

	except TypeError:
		raise ValueError("Error : the function is not applicable to the values")

x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(list(ft_map(lambda t: t + 1, x)))
