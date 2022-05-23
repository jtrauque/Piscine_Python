import numpy as np


class ColorFilter:
    def __init__(self):
        pass

    def invert(self, array): # None authorized except + and - 
        if not isinstance(array, np.ndarray):
            return None
        print(array)
        return 1 - array[:, :, :3]

    def to_blue(self, array): # .zero, .shape, .dstack
        if not isinstance(array, np.ndarray):
            return None
        print(array)
        new = np.zeros((array.shape[0], array.shape[1], 3), dtype=int)
        new[:, :, 2] = array[:, :, 2]
        print(new)
        return new

    def to_green(self, array): # copy.deepcopy + '*'
        if not isinstance(array, np.ndarray):
            return None
        return [0, 1, 0] * array[:, :, :3]

    def to_red(self, array): # .to_green, .to_blue + '-', '+'
        if not isinstance(array, np.ndarray):
            return None
        B = self.to_blue(array)
        G = self.to_green(array)
        return array[:, :, :3] - G - B

    def to_celluloid(self, array): # .arange, .linspace
        if not isinstance(array, np.ndarray):
            return None
        pass

    # .sum,.shape,.tile,.reshape,.dstack,.broadcast_to,.as_type + '*' + '/'
    def to_grayscale(self, array, filter, **kwargs):
        pass

from ImageProcessor import ImageProcessor

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("42AI.png")

    cf = ColorFilter()
    #imp.display(arr)
    #arr2 = cf.invert(arr)
    print(arr)
    imp.display(arr)
    #arr2 = cf.to_blue(arr)
    arr2 = cf.to_green(arr)
    arr2 = cf.to_red(arr)
    print(arr2)
    imp.display(arr2)
