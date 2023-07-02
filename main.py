from PIL import Image
from os import listdir

folder = "sprites"
sprites = [i for i in listdir(folder)]

testImg = Image.open("{}/{}".format(folder, sprites[0]))
imgWidth = testImg.width
imgHeight = testImg.height
del testImg

img = Image.new('RGBA', (imgWidth * len(sprites), imgHeight))
x = 0
for i in sprites:
    sprite = Image.open("{}/{}".format(folder, i))
    img.paste(sprite, (x, 0))
    x += imgWidth
img.save("ss.png")
