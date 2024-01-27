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


def call(top_text, bottom_text, filepath, filename, image_url):
 
    # if image from url, do
    img = download_image(image_url)
    # and put the url as a param of this funct

    #img = Image.open(filepath)
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

    # save the image and continue loop
    img.save("image-outputs/" + filename[:-4] + ".png")
    #img.save("image-outputs/" + filename[:-4] + str(i)+ ".png")
    

def main():
    directory = 'image-resources'
    #i = 0
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if (os.path.isfile(f) and filename[-4:] == (".png")):

            match_name = get_image_word(f)
            
            top_text = match_name
            bottom_text = " "

            call(top_text, bottom_text, f, filename)
            #i = i+1

def main2():
    url1 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Ijms-21-05932-g004.webp/440px-Ijms-21-05932-g004.webp.png"
    url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Coronavirus._SARS-CoV-2.png/220px-Coronavirus._SARS-CoV-2.png"
    filepath = "t"
    filename = "from_wiki"

    match_name = get_image_word(url2)

    call(match_name, "", filepath, filename, url2)


# this calls it 
#call()
#main2()