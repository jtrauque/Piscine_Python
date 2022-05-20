import sys
sys.tracebacklimit = 0


class Vector:
    def __init__(self, args):
        if isinstance(args, int):
            self.values = []
            if args > 0:
                for i in range(0, args):
                    self.values.append([float(i)])
            else:
                raise ValueError('Negative value')
            line = 1
            column = len(self.values)
        elif isinstance(args, tuple) and len(args) == 2:
            self.values = []
            if args[0] > args[1]:
                raise ValueError('Incorrect range')
            if not isinstance(args[0], int) or not isinstance(args[1], int):
                raise TypeError('Incorrect type of input')
            for i in range(args[0], args[1]):
                self.values.append([float(i)])
            line = 1
            column = len(self.values)
        elif isinstance(args, list):
            if isinstance(args[0], list):
                for i in args:
                    for j in i:
                        if not isinstance(j, float):
                            raise ValueError('The list has to contain floats')
                self.values = args
                column = len(args)
                line = 1
            else:
                for i in args:
                    if not isinstance(i, float):
                        raise ValueError('The list has to contain floats')
                self.values = args
                line = len(self.values)
                column = 1
        else:
            raise ValueError('Not the right type of arguments')
        self.shape = (line, column)

    def __add__(self, vec):
        if not isinstance(vec, Vector) or self.shape != vec.shape:
            raise ValueError('Both vectors has to be of the same form')
        new = []
        if self.shape[0] == 1:  # +sieurs column
            for i in range(self.shape[1]):  # we go through the columns
                new.append([self.values[i][0] + vec.values[i][0]])
        else:
            for i in range(self.shape[0]):  # we go through the raws
                new.append(self.values[i] + vec.values[i])
        return Vector(new)

    def __radd__(self, vec):
        return self.__add__(vec)

    def __sub__(self, vec):
        if not isinstance(vec, Vector) or self.shape != vec.shape:
            raise ValueError('Both vectors has to be of the same form')
        new = []
        if self.shape[0] == 1:  # 1 column
            for i in range(self.shape[1]):  # we go through the raws
                new.append([self.values[i][0] - vec.values[i][0]])
        else:
            for i in range(self.shape[0]):  # we go through the columns
                new.append(self.values[i] - vec.values[i])
        return Vector(new)

    def __rsub__(self, vec):
        return self.__sub__(vec)

    def __truediv__(self, div):
        if not isinstance(div, (int, float)) or div == 0:
            raise ValueError('The scalar has to be an int or float \
                             and not zero')
        new = []
        if self.shape[0] == 1:  # 1 column
            for i in range(self.shape[1]):  # we go through the raws
                new.append([self.values[i][0] / div])
        else:
            for i in range(self.shape[0]):  # we go through the columns
                new.append(self.values[i] / div)
        return Vector(new)

    def __rtruediv__(self, div):
        raise ValueError('The scalar cannot be divided by a vector')

    def __mul__(self, mul):
        if not isinstance(mul, (int, float)):
            raise ValueError('The scalar has to be an int or float')
        new = []
        if self.shape[0] == 1:  # 1 column
            for i in range(self.shape[1]):  # we go through the raws
                new.append([self.values[i][0] * mul])
        else:
            for i in range(self.shape[0]):  # we go through the columns
                new.append(self.values[i] * mul)
        return Vector(new)

    def __rmul__(self, mul):
        return self.__mul__(mul)

    def __str__(self):
        return f"Vector shape is : row = {self.shape[0]} and column\
               {self.shape[1]} -- Values = {self.values}"

    def __repr__(self):
        return f"Vector(shape({self.shape}), values({self.values}))"

    def dot(self, mul):
        if not isinstance(mul, Vector) or self.shape != mul.shape:
            raise ValueError('Both vectors has to be of the same form')
        new = []
        if self.shape[0] == 1:  # 1 column
            for i in range(self.shape[1]):  # we go through the raws
                new.append([self.values[i][0] * mul.values[i][0]])
        else:
            for i in range(self.shape[0]):  # we go through the columns
                new.append(self.values[i] * mul.values[i])
        return Vector(new)

    def T(self):
        new = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                new.append(self.values[i][0])
        else:
            for i in range(self.shape[0]):
                new.append([self.values[i]])
        return Vector(new)
