
def ft_reduce(function_to_apply, iterable):
    try:
        if iterable is None or not isinstance(iterable, iter):
            return None
        new = iterable[0]
        for i in iterable[1:]:
            new = function_to_apply(new, i)
        return new

    except TypeError:
        print("Error : the function is not applicable to the values")
        return None


lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
iterable = [1, 2, 3]
print(ft_reduce(lambda u, v: u + v, lst))
print(ft_reduce(None, iterable=iterable))
list(ft_reduce(lambda x: x + 1, None))
