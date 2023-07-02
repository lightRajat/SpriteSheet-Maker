from PIL import Image
from os import listdir

hor = False
folder = "sprites"
sprites = [i for i in listdir(folder)]

testImg = Image.open("{}/{}".format(folder, sprites[0]))
imgWidth = testImg.width
imgHeight = testImg.height
del testImg

img = Image.new('RGBA', (imgWidth * (len(sprites)**hor), imgHeight * ((len(sprites)**int(not(hor))))))
co = 0
for i in sprites:
    sprite = Image.open("{}/{}".format(folder, i))
    img.paste(sprite, (co * hor, co * int(not(hor))))
    co += imgWidth
img.save("ss.png")
