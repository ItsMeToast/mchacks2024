import os
from openai import OpenAI
import random


# Set the OpenAI Key
def get_key():
    file = open("/Users/skylargu/Desktop/API_code.txt", "r")
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

    # print(response.choices[0].message.content)
    return response.choices[0].message.content


def generate_funny_phrase(prompt):
    prompt_list = [
        "Generate a 5 word reddit meme caption about ",
        "Make a short joke about ",
        "Make a 5 word twitter meme about ",
        "Tell me a 5 word joke about ",
        "Tell me something funny about ",
        "Make a 5 word instagram meme caption about ",
        "Make a 5 word wholesome joke about ",
    ]
    rand = random.randint(0, len(prompt_list) - 1)

    # print(prompt_list[rand])

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt_list[rand] + prompt,
            }
        ],
        model="gpt-4-0125-preview",
    )

    phrase = response.choices[0].message.content
    # print(phrase)
    return (rand, phrase)
