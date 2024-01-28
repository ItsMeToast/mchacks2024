import requests


# Function to refresh the website and save random image URLs
def refresh_and_save_urls(num_images):
    image_dict = {}

    for i in range(num_images):
        response = requests.get("https://picsum.photos/2000")

        if response.status_code == 200:
            image_dict[f"Image{i}"] = response.url
            # print(f"Image {i} URL: {response.url}")
        else:
            print(f"Failed to fetch image {i}")

    return image_dict
