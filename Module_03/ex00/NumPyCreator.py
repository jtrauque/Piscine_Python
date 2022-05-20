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
            print("1")
            if not isinstance(lst, list):
                print("2")
                raise TypeError("Incorrect list")
            if isinstance(lst[0], list):
                print("3")
                for i in lst:
                    if len(i) != len(lst[0]):
                         print("Incorrect shape of list")
                         return np
                print("4")
                np = numpy.array(lst)
        except TypeError:
            pass
            #raise TypeError("Incorrect Type")
        return np

    @staticmethod
    def from_tuple(tpl):
        np = None
        try:
            if not isinstance(tpl, tuple):
                raise TypeError("Incorrect Type")
            np = numpy.array(tpl)
        except TypeError:
            raise TypeError("Incorrect Type")
        return np

    @staticmethod
    def from_iterable(itr):
        np = None
        try:
            if not hasattr(itr, "__iter__"):
                raise TypeError("Incorrect Type")
            np = numpy.array(iter)
        except TypeError:
            raise TypeError("Incorrect Type")
        return np

    @staticmethod
    def from_shape(shape, value=0):
        np = None
        try:
            if not isinstance(shape, tuple):
                raise TypeError("Incorrect Type")
            np = numpy.full(shape, value)
        except TypeError:
            raise TypeError("Incorrect Type")
        return np

    @staticmethod
    def random(shape):
        np = None
        try:
            if not isinstance(shape, tuple):
                raise TypeError("Incorrect Type")
            np = numpy.random.random(shape)
        except TypeError:
            raise TypeError("Incorrect Type")
        return np

    @staticmethod
    def identity(n):
        return numpy.array(n)


npc = NumPyCreator()
print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
print(npc.from_list([[1, 2, 3], [6, 4]]))
print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))
#npc.from_list(((1, 2), (3, 4)))
#npc.from_tuple(("a", "b", "c"))
#npc.from_tuple([[1, 2, 3], [6, 3, 4]])
#npc.from_iterable(range(5))
#shape = (3, 5)
#npc.from_shape(shape)
#npc.random(shape)
#npc.identity(4)
