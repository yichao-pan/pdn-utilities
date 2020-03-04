from PIL import Image
import os

def open_image(file):
    """
    Opens image file
    """
    return Image.open(file)

# loop through files in folder
def open_folder(folder, file_type='.png'):
    """
    Loops through image files in a folder and outputs them in a list.
    File type to specify type of file. Uses .png by default
    """
    imgs = []
    for f in os.listdir(folder):
        if f.endswith(file_type):
            imgs.append(Image.open(folder + '/' + f))
    return imgs

def open_txt(file):
    """
    Opens text file
    """
    with open(file + '.txt', 'r') as f:
        return f.read()
