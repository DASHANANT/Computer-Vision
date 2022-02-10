import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('test.jpg')
# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
# Note: always make a copy rather than simply using "="
color_select = np.copy(image)
red_threshold = 190
green_threshold = 208
blue_threshold = 190
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# Identify pixels below the threshold
thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])
# after getting all the positions, which having pixel values less than our threshold,
# we are making it as o
color_select[thresholds] = [0,0,0]

# Display the image                 
plt.imshow(image)
plt.show()
plt.imshow(color_select)
plt.show()