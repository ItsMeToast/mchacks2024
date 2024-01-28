from PIL import Image, ImageEnhance
import numpy as np
import requests
from io import BytesIO

def orange_yellow_deep_fry_from_url(image_url, brightness_factor=1.2, orange_factor=7.5, yellow_factor=1.2, contrast_factor=1.2):
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

    # Increase brightness
    enhancer = ImageEnhance.Brightness(enhanced_image)
    enhanced_image = enhancer.enhance(brightness_factor)

    # Apply contrast enhancement
    enhancer = ImageEnhance.Contrast(enhanced_image)
    contrasted_image = enhancer.enhance(contrast_factor)
    
    return contrasted_image

# Example usage with an image URL
image_url = "https://fastly.picsum.photos/id/676/2000/2000.jpg?hmac=rqDv-Ar51q73E4c0euIyMv1-7YYbJcdZ4II7tn6ly7g"
orange_yellow_deep_fry_from_url(image_url)


