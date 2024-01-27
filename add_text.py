from PIL import Image,ImageDraw,ImageFont
import os


def add_text(draw, text, font, text_x, text_y):
    border_width = 4
    for i in range(-border_width, border_width + 1):
        for j in range(-border_width, border_width + 1):
            draw.text((text_x + i, text_y + j), text, fill="black", font=font)
    draw.text((text_x, text_y), text, fill="white", font=font)


def do_top_text(draw, image, text, font):
    text_width = draw.textlength(text, font=font)

    text_x = (image.width - text_width) // 2
    text_y = 0

    add_text(draw, text, font, text_x, text_y)


def do_bottom_text(draw, image, text, font, font_size):
    text_width = draw.textlength(text, font=font)
    bottom_border = 15

    text_x = (image.width - text_width) // 2
    text_y = (image.height - font_size - bottom_border)

    add_text(draw, text, font, text_x, text_y)


def call():
    
    directory = 'image-resources'
    i = 0

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if (os.path.isfile(f) and filename[-4:] == (".png")):
            #print(f)
            img = Image.open(f)
            draw = ImageDraw.Draw(img)

            top_text = "Bottom Text"
            bottom_text = "real bottom text"

            top_font_size = img.width // len(top_text)
            bottom_font_size = img.width // len(bottom_text)
            top_font = ImageFont.truetype("impact.ttf", top_font_size)
            bottom_font = ImageFont.truetype("impact.ttf", bottom_font_size)


            do_bottom_text(draw, img, bottom_text, bottom_font, bottom_font_size)
            do_top_text(draw, img, top_text, top_font)


            img.save("image-outputs/text" + str(i)+ ".png")
            i = i+1

call()