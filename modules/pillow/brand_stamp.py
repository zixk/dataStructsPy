import os
from PIL import Image, ImageFilter

path = os.path.dirname(__file__)
dirname = path + "/images"
output_dirname = path + "/branded"
images_list = os.listdir(dirname)
logo = Image.open(dirname + "/logo.png")

if not os.path.exists(output_dirname):
    os.makedirs(output_dirname)

for image in images_list:
    name, format = os.path.splitext(image)

    original = Image.open(f'{dirname}\{image}')
    size = (1000,1000)
    original.thumbnail(size)

    image_copy = original.copy()

    position = ((image_copy.width - logo.width),
                (image_copy.height - logo.height))

    image_copy.paste(logo, position, logo)
    image_copy.save(f'{output_dirname}\{name}.png')