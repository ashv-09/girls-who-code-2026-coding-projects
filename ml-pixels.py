"""
ShowPixelGrid: Loads a single row from Fashion MNIST training data,
reshapes pixel values into a 28x28 grid, and displays the image
with pixel values and row/column labels overlaid.
"""

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# SETTINGS
plt.rcParams.update({'font.size': 8})
row_number = 14 # Row to display

# LOAD DATA
df = pd.read_csv('fashion_mnist_20bal_train.csv')

# Extract single row by index
row = df.iloc[row_number]

# PREPARE IMAGE
# Strip label, leaving only pixel values
image_data = row[1:].values

# Convert to unsigned integer for image display
image_data = image_data.astype(np.uint8)

# Reshape pixel values into 28x28 grid
image_28x28 = image_data.reshape(28, 28)

# DISPLAY IMAGE
fig, ax = plt.subplots(figsize=(7, 7))
cax = ax.matshow(image_28x28, cmap='gray')

# Add color bar for reference
plt.colorbar(cax)

# Overlay each pixel's numerical value in red
for (i, j), val in np.ndenumerate(image_28x28):
    ax.text(j, i, val, ha='center', va='center', color='red', fontsize=5)

# Label rows and columns 1-28
ax.set_xticks(np.arange(0, 28, 1))
ax.set_yticks(np.arange(0, 28, 1))
ax.set_xticklabels(np.arange(1, 29, 1))
ax.set_yticklabels(np.arange(1, 29, 1))

plt.show()
