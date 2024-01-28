from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image as tf_image
import numpy as np
from PIL import Image
import os
import requests
from io import BytesIO

# pip3 install tensorflow

def load_and_preprocess_image_resnet50(image_path):
    img = tf_image.load_img(image_path, target_size=(224, 224))
    img_array = tf_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array


def classify_image_resnet50(image):
    model = ResNet50(weights='imagenet')
    
    if isinstance(image, str):  # If the input is a file path
        img_array = load_and_preprocess_image_resnet50(image)
    
    else:  # If the input is an image object
        img_array = tf_image.img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
    
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions)
    
    return decoded_predictions[0]

def display_predictions(predictions):
    for i, (imagenet_id, label, score) in enumerate(predictions):
        return(f"{i + 1}: {label} ({score:.2f})")

def get_highest_match(predictions):
    return predictions[2][1]  # Return the label of the highest match

#def get_image_word(image_path):
#    
#    # Use the ResNet50 model for classification
#    predictions = classify_image_resnet50(image_path)
#    display_predictions(predictions)
#
#    # Get the category with the highest match
#    highest_match_category = get_highest_match(predictions)
#    match = highest_match_category.split("_")
#    match_name = ' '.join(word.capitalize() for word in match)
#
#    return match_name

def get_image_word(image_url):
    try:
        # Download the image from the URL
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
    except Exception as e:
        # Use the ResNet50 model for classification
        predictions = classify_image_resnet50(image_url)
        display_predictions(predictions)

        # Get the category with the highest match
        highest_match_category = get_highest_match(predictions)
        match = highest_match_category.split("_")
        match_name = ' '.join(word.capitalize() for word in match)

        return match_name

    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((224, 224))
    if img.mode != 'RGB':
            img = img.convert('RGB')

    # Use the ResNet50 model for classification
    predictions = classify_image_resnet50(img)
    display_predictions(predictions)

    # Get the category with the highest match
    highest_match_category = get_highest_match(predictions)
    match = highest_match_category.split("_")
    match_name = ' '.join(word.capitalize() for word in match)

    return match_name

