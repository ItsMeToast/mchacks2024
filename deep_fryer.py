import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO


def deep_fry(image_url, brightness_factor=1.2, sharpness_factor=2.0, saturation_factor=2.0):
    # Open the image

    try:
        # Download the image from the URL
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
    except Exception as e:
        image = Image.open(image_url)

    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Increase brightness
    #enhancer = ImageEnhance.Brightness(image)
    #image = enhancer.enhance(brightness_factor)

    # Increase sharpness
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(sharpness_factor)

    # Increase saturation
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(saturation_factor)

    # Apply JPEG compression artifacts (simulating deep frying)
    image = image.filter(ImageFilter.CONTOUR)

    return image


# Example usage
