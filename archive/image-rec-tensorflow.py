from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image as tf_image
import numpy as np
from PIL import Image
import os

def load_and_preprocess_image_resnet50(image_path):
    img = tf_image.load_img(image_path, target_size=(224, 224))
    img_array = tf_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def classify_image_resnet50(image_path):
    model = ResNet50(weights='imagenet')
    img_array = load_and_preprocess_image_resnet50(image_path)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions)
    return decoded_predictions[0]

def display_predictions(predictions):
    for i, (imagenet_id, label, score) in enumerate(predictions):
        return(f"{i + 1}: {label} ({score:.2f})")

def get_highest_match(predictions):
    return predictions[2][1]  # Return the label of the highest match

def main():
    # Take user input for the file
    image_path = input("Enter the image file name: ")

    try:
        image_path = os.path.join('/Users/skylargu/Desktop', image_path)
        img = Image.open(image_path)
        # img.show()
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # Use the ResNet50 model for classification
    predictions = classify_image_resnet50(image_path)
    display_predictions(predictions)

    # Get the category with the highest match
    highest_match_category = get_highest_match(predictions)
    match = highest_match_category.split("_")
    match_name = ' '.join(word.capitalize() for word in match)
    
    print(f"\nThe category with the highest match is: {match_name}")

if __name__ == "__main__":
    main()

