from PIL import Image, ImageEnhance
import numpy as np
import requests
from io import BytesIO

<<<<<<< Updated upstream
def deep_fry_red(image_url, brightness_factor=1.2, orange_factor=7.5, yellow_factor=1.2, contrast_factor=1.2):
=======

def orange_yellow_deep_fry_from_url(
    image_url,
    brightness_factor=1.2,
    orange_factor=7.5,
    yellow_factor=1.2,
    contrast_factor=1.2,
):
>>>>>>> Stashed changes
    # Download the image from the URL
    try:
        # Download the image from the URL
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
    except Exception as e:
        image = Image.open(image_url)

    # Convert the image to RGB (if necessary)
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Apply enhancement to the orange and yellow tones
    img_array = np.array(image)
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
