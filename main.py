from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from openai_api import generate_funny_phrase, detect_image
from image_dictionary import refresh_and_save_urls
from add_text import call
from deep_fryer_red import deep_fry_red
from io import BytesIO
import requests

import cloudinary
from cloudinary import uploader

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
cors = CORS(app)

cloudinary.config( 
  cloud_name = "dh9lwlcpo", 
  api_key = "619834951489553", 
  api_secret = "jCwaUB81jGUNV8Trnp_svwvyoeA" 
)


@app.route('/button_press', methods=['POST'])
def handle_button_press():
    data = request.json  # Assuming JSON data is sent in the request body
    # Call the handler function with the data received from the frontend
    response = handler(data)
    return jsonify(response)

def handler(data):
    # Your handler logic here
    # Process the data received from the frontend
    # print("Button pressed with data:", data)

    image_urls = refresh_and_save_urls(1)
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
        #print("Uploaded image URL:", uploaded_image_url)
        return {'message': uploaded_image_url}

    #return img
    #return {'message': uploaded_image_url}

if __name__ == "__main__":

    app.run(host="localhost", port=5000, debug=True)

#app.run(host="localhost", port=5000)
