import scipy.io
import matplotlib.pyplot as plt

# Load the first .mat file and inspect its keys
data1 = scipy.io.loadmat('img_0334_kernel_x4.mat')
img1 = data1['Kernel']

# Load the second .mat file and inspect its keys
data2 = scipy.io.loadmat('img_0334_kernel_x2.mat')
img2 = data2['Kernel']

# Create a figure with two subplots, side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Display the first image
axes[0].imshow(img1)
axes[0].set_title('Image 1')
axes[0].axis('off')  # Hide axis

# Get and print the dimensions of the first image
dims1 = img1.shape
print(f'Dimensions of Image 1: {dims1}')

# Display the second image
axes[1].imshow(img2)
axes[1].set_title('Image 2')
axes[1].axis('off')  # Hide axis

# Get and print the dimensions of the second image
dims2 = img2.shape
print(f'Dimensions of Image 2: {dims2}')

# Adjust layout and show the images
plt.tight_layout()
plt.show()
