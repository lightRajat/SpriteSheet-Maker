from tkinter import Tk

window = Tk()
window.title("SpriteSheet Maker")

window.mainloop()

##from PIL import Image
##from os import listdir
##
##hor = True
##folder = "sprites"
##sprites = listdir(folder)
##outFolder = "./.."
##outName = "result"
##
##testImg = Image.open("{}/{}".format(folder, sprites[0]))
##imgWidth = testImg.width
##imgHeight = testImg.height
##imgFormat = testImg.format
##del testImg
##
##img = Image.new('RGBA', (imgWidth * len(sprites)**hor, imgHeight * len(sprites)**int(not(hor)) ))
##co = 0
##for i in sprites:
##    sprite = Image.open("{}/{}".format(folder, i))
##    img.paste(sprite, (co * hor, co * int(not(hor))))
##    co += imgWidth
##img.save("{}/{}.{}".format(outFolder, outName, imgFormat.lower()))
