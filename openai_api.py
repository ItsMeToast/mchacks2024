import os
from openai import OpenAI
import random


# Set the OpenAI Key
def get_key():
    file = open("C:\Kieron\School\McGill\Other\McHacks\openai-key.txt", "r")
    key = file.read()

    file.close()
    return key


client = OpenAI(
    # api_key = os.environ.get("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")
    api_key=get_key()
)


def detect_image(url):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in 1-2 words?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": url,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content


def generate_funny_phrase(prompt):
    prompt = prompt
    random_number = str(random.randint(5, 10))
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Generate a"
                + random_number
                + " word reddit meme about"
                + prompt,
            }
        ],
        model="gpt-4-0125-preview",
    )
    phrase = response.choices[0].message.content
    return phrase


# Example Usage:
# if __name__ == "__main__":
# Example prompt
# prompt = "toaster" #make prompt = get_image_word(image_url)

# Generate a funny phrase
# funny_phrase = generate_funny_phrase(prompt)
# print("Funny Phrase:", funny_phrase)
