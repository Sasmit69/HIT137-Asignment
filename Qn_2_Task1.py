import time
from PIL import Image
import numpy as np

# Generate a number based on the current time
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated Number: {generated_number}")

# Define a fraction of the generated number to apply
fraction = 0.1  # Adjust this fraction as needed for a subtle change
adjustment_value = int(generated_number * fraction)

# Open the image file
image_path = 'Chapter1.jpg'
image = Image.open(image_path)

# Convert the image to a NumPy array for processing
image_array = np.array(image)

# Adjust the RGB values by adding the smaller fraction of the generated number
adjusted_image_array = np.clip(image_array + adjustment_value, 0, 255)

# Convert the adjusted array back to an image
adjusted_image = Image.fromarray(adjusted_image_array.astype('uint8'))

# Save the new image
output_image_path = 'chapter1out.jpg'
adjusted_image.save(output_image_path)

# Calculate the sum of all red pixel values in the new image
red_channel = adjusted_image_array[:, :, 0]
sum_red_pixels = np.sum(red_channel)

# Print the sum of red pixel values
print(f"Sum of all red pixel values: {sum_red_pixels}")

