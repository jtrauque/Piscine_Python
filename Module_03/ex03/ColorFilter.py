import numpy as np


class ColorFilter:
    def __init__(self):
        pass

    def invert(self, array): # None authorized except + and - 
        if not isinstance(array, np.ndarray):
            return None
        return 1 - array[:, :, :3]

    def to_blue(self, array): # .zero, .shape, .dstack
        if not isinstance(array, np.ndarray):
            return None
        new = np.zeros((array.shape[0], array.shape[1], 3))
        new[:, :, 2] = array[:, :, 2]
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
            return None
        if filter not in ['m', 'mean', 'w', 'weight']:
            return None
        if filter in ['m', 'mean']:
            R = 0.299
            G = 0.587
            B = 0.114
        else:
            if len(kwarg) != 3:
                return None
            # we neeed 3 args to match RGB and the sum of the should make 1
            lst = list(kwards.values())
            if not all(isinstance(x, float) for x in lst) or sum(lst) != 1:
                return None
            R = lst[0]
            G = lst[1]
            B = lst[2]
        RGB = [R, G, B]
        new = np.broadcast_to(array, array.shape) # on fait une copie
        new = new[..., [0, 1, 2]] * RGB
        tmp = np.sum(new, axis=2, keepdims=True) # gris est la somme de toutes les couleurs
        new = np.broadcast_to(tmp, (array.shape[0], array.shape[1], 3)) # on re repartie cette somme sur tout le reste
        return new

from ImageProcessor import ImageProcessor

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("42AI.png")

    cf = ColorFilter()
    imp.display(arr)
    arr2 = cf.invert(arr)
    #print(arr)
    imp.display(arr2)
    arr2 = cf.to_blue(arr)
    imp.display(arr2)
    arr2 = cf.to_green(arr)
    imp.display(arr2)
    arr2 = cf.to_red(arr)
    imp.display(arr2)
    arr2 = cf.to_celluloid(arr)
    imp.display(arr2)
    arr2 = cf.to_grayscale(arr, 'm')
    #print(arr2)
    imp.display(arr2)
