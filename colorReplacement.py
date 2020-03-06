from PIL import Image
import numpy as np


def replace_color(img, old_color, new_color):
    # "data" is a height x width x 4 numpy array
    img_np = np.array(img)
    # Temporarily unpack the bands for readability
    red, green, blue, alpha = img_np.T
    replaced_areas = (red == old_color[0]) & (blue == old_color[1]) & (green == old_color[2]) & (alpha == old_color[3])
    # Transpose back needed
    img_np[...][replaced_areas.T] = new_color
    img2 = Image.fromarray(img_np)
    return img2

def replace_pallet(img, replace_dict):
    for old_color in replace_dict:
        img = replace_color(img, old_color, replace_dict[old_color])
    return img


def create_replace_dict_img(img, new_row=1):
    """
    Create a color replacement dict from an image
    1st row are old colors
    new_row are replacement colors (default to 1)
    """
    img = img.convert('RGBA')





def create_replace_dict(old_pallet, new_pallet):
    replace_dict = {}
    loop = min(len(old_pallet), len(new_pallet))
    for c in range(0,loop):
        replace_dict[old_pallet[c]] = new_pallet[c]
    return replace_dict
