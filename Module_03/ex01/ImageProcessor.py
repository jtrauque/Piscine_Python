import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self):
        self.array = []
        pass

    def load(self, path):
        image = None
        try:
            if not path or not os.path.exists(path):
                raise ValueError()
            if os.stat(path).st_size == 0:
                raise OSError()
            image = Image.open(path)
            self.array = np.array(image)
            print("Loading image of dimensions " + str(image.size[0]) + " x " + str(image.size[1]))
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
            print("Display error")
            
 
imp = ImageProcessor()
#arr = imp.load("non_existing.png")
#print(arr)           
arr = imp.load("42AI.png")
print(arr)           
#arr = imp.load("empty.png")
#print(arr) 
imp.display(arr)         
