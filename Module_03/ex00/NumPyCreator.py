import numpy
import sys
#sys.tracebacklimit = 0

class NumPyCreator:
    def __init__(self):
        pass

    @staticmethod
    def from_list(lst):
        np = None
        try:
            if not isinstance(lst, list):
                raise TypeError("Incorrect list")
            if isinstance(lst[0], list):
                for i in lst:
                    if len(i) != len(lst[0]):
                         print("Incorrect shape of list")
                         return np
                np = numpy.array(lst)
        except TypeError:
            pass
        return np

    @staticmethod
    def from_tuple(tpl):
        np = None
        try:
            if not isinstance(tpl, tuple):
                raise TypeError("Incorrect Type")
            if isinstance(tpl[0], tuple):
                for i in tpl:
                    if len(i) != len(tpl[0]):
                         print("Incorrect shape of list")
                         return np
            np = numpy.array(tpl)
        except TypeError:
            pass
        return np

    @staticmethod
    def from_iterable(itr):
        np = None
        try:
            if not hasattr(itr, "__iter__"):
                raise TypeError("Incorrect Type")
            np = numpy.array(itr)
        except TypeError:
            pass
        return np

    @staticmethod
    def from_shape(shape, value=0):
        np = None
        try:
            if not isinstance(shape, tuple):
                raise TypeError("Incorrect Type")
            np = numpy.full(shape, value)
        except TypeError:
            pass
        return np

    @staticmethod
    def random(shape):
        np = None
        try:
            if not isinstance(shape, tuple):
                raise TypeError("Incorrect Type")
            np = numpy.random.random(shape)
        except TypeError:
            pass
        return np

    @staticmethod
    def identity(n):
        return numpy.identity(n)


npc = NumPyCreator()
print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
print(npc.from_list([[1, 2, 3], [6, 4]]))
print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))
print(npc.from_list(((1, 2), (3, 4))))
print(npc.from_tuple(("a", "b", "c")))
print(npc.from_tuple([[1, 2, 3], [6, 3, 4]]))
print(npc.from_iterable(range(5)))
shape = (3, 5)
print(npc.from_shape(shape))
print(npc.random(shape))
print(npc.identity(4))
