import sys
sys.tracebacklimit = 0


def ft_map(function_to_apply, iterable):
    try:
        for i in iterable:
            yield function_to_apply(i)

    except TypeError:
        print("Error : the function is not applicable to the values")
        return None


x = [1, 2, 3, 4, 5]
iterable = [1, 2, 3]
print(ft_map(lambda dum: dum + 1, x))
print(list(ft_map(lambda t: t + 1, x)))
print(ft_map(function_to_apply=None, iterable=iterable))
list(ft_map(function_to_apply=None, iterable=iterable))
