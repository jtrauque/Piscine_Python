
def ft_filter(function_to_apply, iterable):
    try:
        for i in iterable:
            if function_to_apply(i):
                yield i

    except TypeError:
        print("Error : the function is not applicable to the values")
        return None


x = [1, 2, 3, 4, 5]
iterable = [1, 2, 3]
print(ft_filter(lambda dum: not (dum % 2), x))
print(list(ft_filter(lambda dum: not (dum % 2), x)))
print(ft_filter(function_to_apply=None, iterable=iterable))
list(ft_filter(function_to_apply=None, iterable=iterable))
