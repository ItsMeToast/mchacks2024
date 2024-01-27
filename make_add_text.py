
### NOT USED ###


from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image as tf_image
import numpy as np
from PIL import Image,ImageDraw,ImageFont
import os

# pip3 install pillow, tensorflow

## tensor flow ##

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


## adding text ##

def add_text(draw, text, font, text_x, text_y):
    border_width = 4
    for i in range(-border_width, border_width + 1):
        for j in range(-border_width, border_width + 1):
            draw.text((text_x + i, text_y + j), text, fill="black", font=font)
    draw.text((text_x, text_y), text, fill="white", font=font)

def find_centre_x(draw, image, font, text):
    text_width = draw.textlength(text, font=font)
    text_x = (image.width - text_width) // 2

    return text_x


def do_top_text(draw, image, text, font):

    text_x = find_centre_x(draw, image, font, text)
    text_y = 0

    add_text(draw, text, font, text_x, text_y)


def do_bottom_text(draw, image, text, font, font_size):
    bottom_border = 15

    text_x = find_centre_x(draw, image, font, text)
    text_y = (image.height - font_size - bottom_border)

    add_text(draw, text, font, text_x, text_y)


## mains ##

def main():
    # Take user input for the file
    #image_path = input("Enter the image file name: ")

    directory = 'image-resources'
    i = 0

    for filename in os.listdir(directory):
        image_path = os.path.join(directory, filename)
        if (os.path.isfile(image_path) and filename[-4:] == (".png")):

            img = Image.open(image_path)
            draw = ImageDraw.Draw(img)


            # get prediction
            predictions = classify_image_resnet50(image_path)
            display_predictions(predictions)

            highest_match_category = get_highest_match(predictions)
            match = highest_match_category.split("_")
            match_name = ' '.join(word.capitalize() for word in match)

            # if import text, change here
            top_text = match_name
            bottom_text = "."

            # calculating text size and setting it 
            top_font_size = img.width // len(top_text)
            bottom_font_size = img.width // len(bottom_text)
            top_font = ImageFont.truetype("impact.ttf", top_font_size)
            bottom_font = ImageFont.truetype("impact.ttf", bottom_font_size)

            # putting the text on the image
            do_bottom_text(draw, img, bottom_text, bottom_font, bottom_font_size)
            do_top_text(draw, img, top_text, top_font)

            # save the image and continue loop
            img.save("image-outputs/" + filename[:-4] + str(i)+ ".png")
            i = i+1

    #try:
    #    image_path = os.path.join('/Users/skylargu/Desktop', image_path)
    #    img = Image.open(image_path)
        # img.show()
    #except Exception as e:
    #    print(f"Error loading image: {e}")
    #    return

    # Use the ResNet50 model for classification
    

    # Get the category with the highest match
    
    
    #print(f"\nThe category with the highest match is: {match_name}")

    

# this calls it 
main()