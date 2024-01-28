from PIL import Image, ImageEnhance
import numpy as np
import requests
from io import BytesIO

def deep_fry_red(image_url, fry_level=3, orange_factor=6.5, yellow_factor=1.2, brightness_factor=1.4, contrast_factor=1.2):
    # deep fries image based on fry_level
    if fry_level == 1:
        brightness_factor, orange_factor, yellow_factor = [1, 1, 1]
    if fry_level == 2:
        brightness_factor *= 0.35
        orange_factor *= 0.35
        
    # Download the image from the URL
    response = requests.get(image_url)
    original_image = Image.open(BytesIO(response.content))

    # Convert the image to RGB (if it's not already)
    original_image = original_image.convert('RGB')

    # Apply enhancement to the orange and yellow tones
    img_array = np.array(original_image)
    img_array[:, :, 0] = np.clip(img_array[:, :, 0] * orange_factor, 0, 255)
    img_array[:, :, 1] = np.clip(img_array[:, :, 1] * yellow_factor, 0, 255)

    # Convert the modified array back to an image
    enhanced_image = Image.fromarray(img_array)

    enhancer_b = ImageEnhance.Brightness(enhanced_image)
    enhancer_c = ImageEnhance.Contrast(enhanced_image)
    
    if fry_level != 1:
        enhanced_image = enhancer_b.enhance(brightness_factor)
        enhanced_image = enhancer_c.enhance(contrast_factor)

    # Show the enhanced image
    enhanced_image.show()

# Example usage with an image URL




