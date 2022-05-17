
def	ft_filter(function_to_apply, iterable):
	try:
		for i in iterable:
			if function_to_apply(i):
				yield i 
	
	except TypeError:
		raise ValueError("Error : the function is not applicable to the values")

x = [1, 2, 3, 4, 5]
print(ft_filter(lambda dum: not (dum % 2), x))
print(list(ft_filter(lambda dum: not (dum % 2), x)))
