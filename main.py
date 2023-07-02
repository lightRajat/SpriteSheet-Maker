from PIL import Image

img1 = Image.open("1.png")
img2 = Image.open("2.png")

img = Image.new('RGBA', (128, 64))
img.paste(img1, (0, 0))
img.paste(img2, (img1.width, 0))
img.save("ss.png")
