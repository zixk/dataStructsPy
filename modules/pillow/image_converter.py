import os
from PIL import Image

path = os.path.dirname(__file__)
dirname = path + "/images"
output_dirname = path + "/generated"
images_list = os.listdir(dirname)

if not os.path.exists(output_dirname):
    os.makedirs(output_dirname)

for image in images_list:
    name, format = os.path.splitext(image)
    original = Image.open(f'{dirname}\{image}')

    size = (1000,1000)
    original.thumbnail(size)

    original.save(f'{output_dirname}\{name}.png')
