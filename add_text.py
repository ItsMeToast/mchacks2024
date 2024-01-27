from PIL import Image,ImageDraw,ImageFont

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
    img = Image.open("Image_created_with_a_mobile_phone.png")
    draw = ImageDraw.Draw(img)

    font_size = 148
    font = ImageFont.truetype("impact.ttf", font_size)

    top_text = "Bottom text"
    bottom_text = "real bottom text"

    do_bottom_text(draw, img, bottom_text, font, font_size)
    do_top_text(draw, img, top_text, font)

    img.save("text.png")

call()