from PIL import Image
from os import listdir

folder = "sprites"
sprites = [i for i in listdir(folder)]

img = Image.new('RGBA', (len(sprites) * 64, 64))
x = 0
for i in sprites:
    sprite = Image.open("{}/{}".format(folder, i))
    img.paste(sprite, (x, 0))
    x += 64
img.save("ss.png")
