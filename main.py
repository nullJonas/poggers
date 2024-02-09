# comentario

from PIL import Image
import numpy as np

def apply_convolution(image, kernel):
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Get dimensions of the image
    height, width, channels = image_array.shape
    
    # Get dimensions of the kernel
    k_height, k_width = kernel.shape
    
    # Pad the image to handle boundary pixels
    pad_height = k_height // 2
    pad_width = k_width // 2
    padded_image = np.pad(image_array, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)), mode='edge')
    
    # Apply convolution for each color channel separately
    output_array = np.zeros_like(image_array, dtype=np.float32)
    for c in range(channels):
        for i in range(height):
            for j in range(width):
                output_array[i, j, c] = np.sum(padded_image[i:i+k_height, j:j+k_width, c] * kernel)
    
    # Clip values to ensure they are within 0-255 range
    output_array = np.clip(output_array, 0, 255)
    
    # Convert output array back to image
    output_image = Image.fromarray(output_array.astype(np.uint8), mode=image.mode)
    
    return output_image

# Read input image
filename = input("Insira o nome do arquivo: ")
input_image = Image.open(filename)

# Define a simple 3x3 kernel for edge detection
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

# Apply convolution
output_image = apply_convolution(input_image, kernel)

# Display original and convolved images
input_image.show(title="Original Image")
output_image.show(title="Convolved Image")
