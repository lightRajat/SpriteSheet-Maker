from tkinter import Tk, Frame, Radiobutton, IntVar, Label, Entry, Button, Scrollbar, Listbox, filedialog

def selectFolder():
    eSrc.config(state = 'normal')
    bSrc.config(command = srcBrowseFolder)

def selectFiles():
    eSrc.config(state = 'disabled')
    bSrc.config(command = srcBrowseFiles)

def srcBrowseFolder():
    print("fubar")

def srcBrowseFiles():
    print("fubar2")

## Main Window 
window = Tk()
window.title("SpriteSheet Maker")

mainFrame = Frame(master = window)
mainFrame.pack(fill = 'both', expand = 'true', padx = 10, pady = 10)

## Frame 1 - Source
frame1 = Frame(master = mainFrame)
frame1.pack(pady = 3)

src = IntVar()

rFolder = Radiobutton(master = frame1, text = "Folder", variable = src, value = 1, command = selectFolder)
rFolder.pack(side = 'left')
rFolder.select()

rFiles = Radiobutton(master = frame1, text = "Multiple Files", variable = src, value = 2, command = selectFiles)
rFiles.pack(side = 'right')

## Frame 2 - File Selection
frame2 = Frame(master = mainFrame)
frame2.pack(pady = 3)

lSrc = Label(master = frame2, text = "Source Folder: ")
lSrc.pack(side = 'left')


eSrc = Entry(master = frame2, width = 50)
eSrc.pack(side = 'left')
eSrc.insert(0, "D:\Dinu\Spaces\Python\practice\ssMaker")

bSrc = Button(master = frame2, text = "Browse", command = srcBrowseFolder)
bSrc.pack(side = 'left', padx = 10)

## Frame 3 - Files
frame3 = Frame(master = mainFrame)
frame3.pack(pady = 3)

lFiles = Label(master = frame3, text = "Sprites\nSelected: ")
lFiles.pack(side = 'left')

lbFiles = Listbox(master = frame3)
lbFiles.pack(side = 'left')

sbFiles = Scrollbar(master = frame3)
sbFiles.pack(side = 'left', fill = 'both')

lbFiles.config(yscrollcommand = sbFiles.set)
sbFiles.config(command = lbFiles.yview)

## Frame 4 - Orientation
frame4 = Frame(master = mainFrame)
frame4.pack(pady = 3)

lOrien = Label(master = frame4, text = "Orientation: ")
lOrien.pack(side = 'left')

orien = IntVar()

rOrien = Radiobutton(master = frame4, text = "Horizontal", variable = orien, value = 1)
rOrien.pack(side = 'left')
rOrien.select()

rOrien = Radiobutton(master = frame4, text = "Vertical", variable = orien, value = 2)
rOrien.pack(side = 'right')

## Frame 5 - Output
frame5 = Frame(master = mainFrame)
frame5.pack(pady = 3)

lOut = Label(master = frame5, text = "Output: ")
lOut.pack(side = 'left')

eOut = Entry(master = frame5, width = 55)
eOut.pack(side = 'left')
eOut.insert(0, "D:\Dinu\Spaces\Python\practice\ssMaker\spritesheet.png")

bOut = Button(master = frame5, text = "Browse")
bOut.pack(side = 'left', padx = 10)

## Area 6 - Log
lLog = Label(master = mainFrame, text = "--Log--")
lLog.pack(pady = 3)

## Area 7 - Submit
bSubmit = Button(master = mainFrame, text = "Make")
bSubmit.pack(pady = 3)

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
