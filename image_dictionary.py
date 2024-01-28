import requests

# Function to refresh the website and save image URLs
def refresh_and_save_urls(num_images, base_url='https://picsum.photos/2000'):
    image_dict = {}

    for i in range(1, num_images + 1):
        url = f"{base_url}?refresh={i}"
        response = requests.get(url)
        
        if response.status_code == 200:
            image_dict[f'Im_{i}'] = response.url
            print(f"Image {i} URL: {response.url}")
        else:
            print(f"Failed to fetch image {i}")

    return image_dict

# Example usage
#base_url = 'https://picsum.photos/2000' # this URL generates square images with dimension 2000
#num_images = 90

#image_urls = refresh_and_save_urls(base_url, num_images)
#print(image_urls)
