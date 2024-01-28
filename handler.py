import os

from image_rec_tensorflow_2 import get_image_word 
from add_text import call
from deep_fryer import deep_fry


def main():
    # this one is for image files

    directory = 'image-resources'
    i = 0
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if (os.path.isfile(f) and filename[-4:] == (".png")):

            match_name = get_image_word(f)
            
            top_text = match_name
            bottom_text = ""

            call(top_text, bottom_text, f, filename, "")
            i = i+1

def main2():
    # this one is for image urls

    url1 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Ijms-21-05932-g004.webp/440px-Ijms-21-05932-g004.webp.png"
    url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Coronavirus._SARS-CoV-2.png/220px-Coronavirus._SARS-CoV-2.png"
    filepath = "t"
    filename = "from_wiki"

    match_name = get_image_word(url2)

    call(match_name, "", filepath, filename, url2)

def main3():
    # this one is for image files deep fried

    directory = 'image-resources/'
    save_dir = "image-outputs/"
    #filename = "heart-thumbs-up.png"
    #filepath = directory + filename

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if (os.path.isfile(filepath) and filename[-4:] == (".png")):

            match_name = get_image_word(filepath)
            img = deep_fry(filepath)
            
            top_text = match_name
            bottom_text = ""

            img = call(match_name, "", img)
            
            img.save(save_dir + filename[:-4] + ".png")

            #i = i+1
    
def main4():
    directory = 'image-resources/'
    save_dir = "image-outputs/"
    filename = "rain.png"
    filepath = directory + filename

    match_name = get_image_word(filepath)
    img = deep_fry(filepath)
    
    top_text = match_name
    bottom_text = ""

    img = call(match_name, "", img)
    img.save(save_dir + filename[:-4] + ".png")

    


main4()