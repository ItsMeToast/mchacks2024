import os
from openai import OpenAI
import random

# Set your OpenAI GPT-3 API key
client = OpenAI(
    #api_key = os.environ.get("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")
    api_key = "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"
)

def generate_funny_phrase(prompt):
    prompt = prompt
    random_number = str(random.randint(5, 10))
    response = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": "Generate a" + random_number + "word meme about" + prompt,
        }
    ],
    model="gpt-4-0125-preview",
)
    phrase = response.choices[0].message.content
    return phrase

# Example Usage:
#if __name__ == "__main__":
    # Example prompt
    #prompt = "toaster" #make prompt = get_image_word(image_url) 

    # Generate a funny phrase
    #funny_phrase = generate_funny_phrase(prompt)
    #print("Funny Phrase:", funny_phrase)
