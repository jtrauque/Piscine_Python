
def	ft_reduce(function_to_apply, iterable):
	try:
		new = iterable[0]
		for i in iterable[1:]:
			new = function_to_apply(new, i)
		return new
	
	except TypeError:
		raise ValueError("Error : the function is not applicable to the values")

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))		
