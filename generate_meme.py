from openai_api import generate_funny_phrase, detect_image
from image_dictionary import refresh_and_save_urls
from add_text import call
from deep_fry_red import deep_fry_red

num_images = 10
image_urls = refresh_and_save_urls(num_images)
save_dir = "image-outputs/"

for num, url in image_urls.items():
    # Uses OpenAI vision to detect subject of image
    match_name = detect_image(url)
    # Generates funny caption based on subject of image
    text = generate_funny_phrase(match_name)

    img = orange_yellow_deep_fry_from_url(url)
    img = call(text, img)

    img.save(save_dir + str(num) + ".png")
