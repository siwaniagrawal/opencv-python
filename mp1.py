import numpy as np
import cv2
from matplotlib import pyplot as plt
img = plt.imread('q.png',0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
