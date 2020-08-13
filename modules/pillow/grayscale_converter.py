import os
from PIL import Image, ImageFilter

path = os.path.dirname(__file__)
dirname = path + "/images"
output_dirname = path + "/greyscale"
images_list = os.listdir(dirname)

if not os.path.exists(output_dirname):
    os.makedirs(output_dirname)

for image in images_list:
    name, format = os.path.splitext(image)

    original = Image.open(f'{dirname}\{image}')
    size = (1000,1000)
    original.thumbnail(size)

    grayscale_image = original.convert('L')
    grayscale_image.save(f'{output_dirname}\{image}')
