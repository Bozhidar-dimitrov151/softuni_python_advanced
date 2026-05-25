import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from skimage import data, io, filters
from scipy.ndimage import convolve

image = "download.jfif"

image_df = io.imread(image)

r = image_df[:,:, 0]
g = image_df[:,:, 1]
b = image_df[:,:, 2]

# plt.imshow(g, cmap="grey")
# plt.show()

kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

filtered = convolve(g, kernel)

plt.imshow(filtered, cmap="grey")
plt.show()