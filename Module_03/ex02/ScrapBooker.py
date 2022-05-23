import numpy as np


class ScrapBooker:
    def crop(self, array, dim, position=(0, 0)):
        if not isinstance(dim, tuple) or not isinstance(position, tuple):
            return None
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dim[0], int) or not isinstance(dim[1], int)\
           or not isinstance(position[0], int)\
           or not isinstance(position[1], int):
            return None
        if dim[0] < 0 or dim[1] < 0 or position[0] < 0 or position[1] < 0:
            return None
        return array[position[0]:dim[0] + position[0],
                     position[1]:dim[1] + position[1]]

    def thin(self, array, n, axis):
        if not n > 0 or not n < array.shape[0]:
            print("1")
            return None
        if not isinstance(array, np.ndarray):
            print("2")
            return None
        if axis != 0 and axis != 1:
            print("3")
            return None
        return np.delete(array, range(n - 1, array.shape[axis], n), axis)
    # range(start, stop, on avance de n de l un a l autre)

    def juxtapose(self, array, n, axis):
        if not n > 0:
            print("1")
            return None
        if not isinstance(array, np.ndarray):
            print("2")
            return None
        if axis != 0 and axis != 1:
            print("3")
            return None
        new = array
        for i in range(n - 1):
            new = np.concatenate((new, array), axis)
        return new

    def mosaic(self, array, dim):
        if not isinstance(dim, tuple):
            return None
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dim[0], int) or not isinstance(dim[1], int):
            return None
        if dim[0] < 0 or dim[1] < 0:
            return None
        new = self.juxtapose(array, dim[0], 0)
        new = self.juxtapose(new, dim[1], 1)
        return new


spb = ScrapBooker()

print("-------------CROP--------------")
arr1 = np.arange(0, 25).reshape(5, 5)
print(arr1)
print(spb.crop(arr1, (3, 1), (1, 0)))

print("-------------THIN--------------")
arr2 = np.array(" A B C D E F G H I".split() * 6).reshape(-1, 9)
print(arr2)
print(spb.thin(arr2, 3, 1))

print("-------------JUX--------------")
arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(arr3)
print(spb.juxtapose(arr3, 3, 1))

print("-------------MOSAIC--------------")
arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(arr3)
print(spb.mosaic(arr3, (3, 3)))
