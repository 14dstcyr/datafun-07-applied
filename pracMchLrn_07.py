from string import digits
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits

digits = load_digits()  # Load the digits dataset

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))

# Displaying Each Image and Removing the Axes Labels 
for ax, image, target in zip(axes.ravel(), digits.images, digits.target):
    ax.imshow(image, cmap=plt.cm.gray_r)
    ax.set_xticks([])  # remove x-axis tick marks
    ax.set_yticks([])  # remove y-axis tick marks
    ax.set_title(target)

plt.tight_layout()
plt.show()     