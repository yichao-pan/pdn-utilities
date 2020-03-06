from fileIO import *
from rgbHexConvert import *
from PIL import Image


def img_to_str_pallet(img):
    """
    Converts an image into a pdn pallet style text file
    """
    img = img.convert('RGBA')
    x_size, y_size = img.size
    pallet_list = []
    for y in range(0, y_size):
        for x in range(0, x_size):
            h = rgba_to_hex(img.getpixel((x, y)), True)
            h = h.lstrip('#')
            h = h.upper()
            pallet_list.append(h)
    return pallet_list


def str_to_img_pallet(pallet_list):
    """
    Converts a list of strings into a pdn pallet style image
    """
    img = Image.new(mode="RGBA", size=(16, 6))
    i = 0
    for y in range(0, 6):
        for x in range(0, 16):
            if (i < len(pallet_list)):
                img.putpixel((x, y), hex_to_rgba(pallet_list[i], pdn=True))
                i = i + 1
            else:
                img.putpixel((x, y), (255,255,255))

    return img


def save_img_pallet(pallet_list, file):
    """
    Convert an image into a pdn pallet text file and save it
    """
    img = str_to_img_pallet(pallet_list)
    save_img(file + '.png')

def save_str_pallet(img, file):
    """
    Convert a pdn pallet text file into an image
    """
    lst = img_to_str_pallet(img)
    save_list_txt(lst, file + '.txt')
