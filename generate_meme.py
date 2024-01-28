from openai_api import generate_funny_phrase, detect_image
from image_dictionary import refresh_and_save_urls
from add_text import call
from deep_fryer_red import deep_fry_red


def generate_meme(num_images):
    image_urls = refresh_and_save_urls(num_images)
    save_dir = "image-outputs/"

    for num, url in image_urls.items():
        # Uses OpenAI vision to detect subject of image
        match_name = detect_image(url)
        # Generates funny caption based on subject of image
        fry_level, text = generate_funny_phrase(match_name)

        img = deep_fry_red(url, int(fry_level))
        img = call(text, img)

        img.save(save_dir + str(num) + ".png")

        return img


generate_meme(2)
