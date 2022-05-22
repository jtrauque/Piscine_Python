import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        if not isinstance(dim, tuple) or not isinstance(position, tuple):
            print("1")
            return None
        if not isinstance(array, np.ndarray):
            print("2")
            return None
        if not isinstance(dim[0], int) or not isinstance(dim[1], int)\
               or not isinstance(position[0], int) or not isinstance(position[1], int):
            #print("3", np.linalg.eigvals(array))
            return None
        if dim[0] < 0 or dim[1] < 0 or position[0] < 0 or position[1] < 0:
            print("4")
            return None
        return array[position[0]:dim[0] + position[0],
                    position[1]:dim[1] + position[1]]

    def thin(self, array, n, axis):
        pass
    def juxtapose(self, array, n, axis):
        pass
    def mosaic(self, array, dim):
        pass


spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(arr1)
print(spb.crop(arr1, (3,1),(1,0)))

arr2 = np.array(" A B C D E F G H I".split() * 6)
print(arr2)
arr2 = np.array(" A B C D E F G H I".split() * 6).reshape(-1,9)
print(arr2)
