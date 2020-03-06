from PIL import Image
import os


def open_image(file):
    """
    Opens image file
    """
    return Image.open(file)


def save_img(img, file):
    img.save(file)


def open_txt(file):
    """
    Opens text file
    """
    with open(file, 'r') as f:
        return f.read()


def save_list_txt(lst, file):
    """
    Saves list as text file
    """
    with open(file, 'w') as f:
        for item in lst:
            f.write("%s\n" % item)


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
