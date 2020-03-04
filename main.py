from PIL import Image, ImageColor
import os
from pdnPallet import *
from rgbHexConvert import *
from fileIO import *
import numpy as np



folder = './images'

# print(hex_to_rgba('#ffffff'))
f = open_txt('test')
f = f.split('\n')
save_img_pallet(f, 'test2')


# img = get_files(folder)[0]
# save_str_pallet(img,'test')


# img.putpixel((0, 0), (255, 0, 0, 255))
# img.save(folder + '/test1.png')
