from PIL import Image,ImageDraw,ImageFont
import os
import requests
from io import BytesIO

from image_rec_tensorflow_2 import get_image_word 


# pip3 install pillow

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


def download_image(image_url):
    # NOT CURRENTLY USED - if using urls to get images
    # image_url = "https://example.com/image.jpg"

    # Download  image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    return image


def upload_image(saved_filename):
    # OPTIONAL - NOT CURRENTLY USED

    upload_url = "https://example.com/upload"
    files = {'file': open(saved_filename, 'rb')}
    
    upload_response = requests.post(upload_url, files=files)

    # The URL of the uploaded image will typically be provided in the response from the server
    uploaded_image_url = upload_response.json()["url"]


def call(top_text, bottom_text, img):
    # leave image url as an empty string if it's not used

    #if (image_url == ""):
    #    img = Image.open(filepath)
    #else:
    #    img = download_image(image_url)
    
    draw = ImageDraw.Draw(img)

    # as to not divide by 0 later
    if len(top_text) == 0:
        top_text = " "
    if len(bottom_text) == 0:
        bottom_text = " "

    # calculating text size and setting it 
    top_font_size = img.width // len(top_text)
    bottom_font_size = img.width // len(bottom_text)
    top_font = ImageFont.truetype("impact.ttf", top_font_size)
    bottom_font = ImageFont.truetype("impact.ttf", bottom_font_size)

    # putting the text on the image
    do_bottom_text(draw, img, bottom_text, bottom_font, bottom_font_size)
    do_top_text(draw, img, top_text, top_font)

    # save the image in a folder
    
    return img
    
    #save_dir = "image-outputs/"
    #img.save(save_dir + filename[:-4] + ".png")
    
