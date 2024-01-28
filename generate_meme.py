from openai_api import generate_funny_phrase, detect_image
from image_dictionary import refresh_and_save_urls
from add_text import call
from deep_fryer_red import deep_fry_red
from io import BytesIO
import requests

import cloudinary
from cloudinary import uploader

          
cloudinary.config( 
  cloud_name = "dh9lwlcpo", 
  api_key = "619834951489553", 
  api_secret = "jCwaUB81jGUNV8Trnp_svwvyoeA" 
)

def generate_meme(num_images):
    image_urls = refresh_and_save_urls(num_images)
    save_dir = "image-outputs/"
    # print(image_urls)

    for num, url in image_urls.items():
        # Uses OpenAI vision to detect subject of image
        match_name = detect_image(url)
        # Generates funny caption based on subject of image
        fry_level, text = generate_funny_phrase(match_name)

        img = deep_fry_red(url, fry_level)
        img = call(text, img)

        #img.save(save_dir + str(num) + ".png")

        upload_url = "https://example.com/upload"
        image_bytes = BytesIO()

        img.save(image_bytes, format='PNG')
        image_bytes.seek(0)

        # Upload the image bytes to Cloudinary
        upload_result = uploader.upload(image_bytes, folder="example_folder")

        # Access the uploaded image URL
        uploaded_image_url = upload_result['secure_url']
        print("Uploaded image URL:", uploaded_image_url)
        return uploaded_image_url

    #return img


#generate_meme(2)
