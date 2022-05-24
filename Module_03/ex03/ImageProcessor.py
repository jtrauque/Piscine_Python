import os
import numpy as np
#from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import image


class ImageProcessor:
    def __init__(self):
        self.array = []
        pass

    def load(self, path):
        try:
            if not path or not os.path.exists(path):
                raise ValueError()
            if os.stat(path).st_size == 0:
                raise OSError()
            #image = Image.open(path)
            img = image.imread(path)
            self.array = np.array(img)
            print("Loading image of dimensions " + str(img.shape[0]) + " x " + str(img.shape[1]))
        except ValueError:
            print("FileNotFoundError -- strerror: No such file or directory")
        except OSError:
            print("OSError -- strerror:")
        return self.array
         
    def display(self, array):
        try:
            imgplot = plt.imshow(array)
            plt.show()
        except Exception as msg:
            print("Display error :", msg)
