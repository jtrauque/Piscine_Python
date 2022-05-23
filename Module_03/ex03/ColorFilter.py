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
        inter = np.linspace(0, 1, 5)
        for i in np.arange(1, 5):
            array[(array>=inter[i - 1]) & (array<inter[i])] = inter[i - 1]
        return array

    def to_grayscale(self, array, filter, **kwargs):
        if array is None or not isinstance(array, np.ndarray):
            print("1")
            return None
        if filter not in ['m', 'mean', 'w', 'weight']:
            print("2")
            return None
        if filter in ['m', 'mean']:
            print("3")
            #return np.dstack((np.sum(array, -1), np.sum(array, -1), np.sum(array, -1))) / 3
            #new = [0.299, 0.587, 0.114] * array[:, :, :3]
            ret = np.sum(array[..., :3], axis=2, keepdims=True) / 3
            return np.dstack((np.tile(ret, 3), array[..., 3:]))
        else:
            print("4")
            ret = np.sum(array[..., :3], axis=2, keepdims=True)
            return np.dstack((np.tile(ret, 3), array[..., 3:]))
           # num = NumPyCreator()
            #weight = num.from_list(weight)
            #if weight and weight.shape[0] == 3 and np.sum(weight, axis=0) == 1.0 and\
              # np.sum(((weight >=0) & (weight <=1)).astype(int)) == 3:
              #  ret = np.sum(array * np.broadcast_to(weight, array.shape), -1) /3
               # return np.dstack((ret, ret, ret))

        # .sum,.shape,.tile,.reshape,.dstack,.broadcast_to,.as_type + '*' + '/'
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
    #arr2 = cf.to_green(arr)
    #arr2 = cf.to_red(arr)
    #arr2 = cf.to_celluloid(arr)
    arr2 = cf.to_grayscale(arr, 'm')
    #print(arr2)
    imp.display(arr2)
