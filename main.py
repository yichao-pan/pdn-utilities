from PIL import Image, ImageColor
import os

from pdnPallet import *
from rgbHexConvert import *
from colorReplacement import *
from fileIO import *

folder = './images'

old_colors = [(0, 0, 0, 255),
                (255, 0, 0, 255)
              ]
new_colors = [(200, 180, 50, 255),
            (12, 200, 50, 255)
              ]


img = open_image(folder + '/img0.png')
img = img.convert('RGBA')

replace_dict = create_replace_dict(old_colors, new_colors)

img2 = replace_pallet(img, replace_dict)
img2.show()
