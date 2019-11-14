import numpy as np
from skimage import io
from skimage.color import rgb2lab, deltaE_cie76
import matplotlib.pyplot as plt

rgb = io.imread('https://i.stack.imgur.com/npnrv.png')
print(rgb)
lab = rgb2lab(rgb)
print(lab)

green = [0, 160, 0]
magenta = [120, 0, 140]

threshold_green = 15    
threshold_magenta = 20    

green_3d = np.uint8(np.asarray([[green]]))
magenta_3d = np.uint8(np.asarray([[magenta]]))

dE_green = deltaE_cie76(rgb2lab(green_3d), lab)
dE_magenta = deltaE_cie76(rgb2lab(magenta_3d), lab)
# print(dE_green)

rgb[dE_green < threshold_green] = green_3d
rgb[dE_magenta < threshold_magenta] = magenta_3d
io.imshow(rgb)
plt.show()