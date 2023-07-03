from tkinter import Tk, Frame, Radiobutton, BooleanVar, Label, Entry, Button, Scrollbar, Listbox, filedialog
from os import listdir, getcwd
from PIL import Image

horz = None # True (later in code)
sprites = list()
currDir = getcwd()
output = currDir + "\spritesheet.png"

def selectFolder():
    lSrc.config(state = 'normal')
    lSrcLoc.config(state = 'normal')
    bSrc.config(command = srcBrowseFolder)
    log(0)

def selectFiles():
    lSrc.config(state = 'disabled')
    lSrcLoc.config(state = 'disabled')
    bSrc.config(command = srcBrowseFiles)
    log(1)

def srcBrowseFolder():
    folder = filedialog.askdirectory(title = "Select the folder containing Sprites", initialdir = currDir)
    if folder:
        lSrcLoc.config(text = folder)
        updateFiles(["{}/{}".format(folder, i) for i in listdir(folder)])

def srcBrowseFiles():
    files = filedialog.askopenfilenames(title = "Select one or more sprites", filetypes = (("Image Files", '*.jpg *.jpeg'), ("Image Files", '*.png')), initialdir = currDir)
    if files:
        global sprites
        updateFiles(files)

def updateFiles(files):
    global sprites
    x = 0
    for i in files:
        if i not in sprites:
            x += 1
            sprites.append(i)
            lbFiles.insert('end', extractNames(i))
            bClear.config(state = 'normal')
            bSubmit.config(state = 'normal')
    log(2, x)

def extractNames(path):
    return path[path.rfind('/') + 1:]

def clearList():
    sprites.clear()
    lbFiles.delete(0, 'end')
    bClear.config(state = 'disabled')
    bSubmit.config(state = 'disabled')
    log(3)

def outBrowse():
    out = filedialog.asksaveasfilename(title = "Save As", filetypes = (("PNG File", '*.png'), ("JPG File", '*.jpg *.jpeg')), initialdir = currDir, defaultextension = '.png')
    if out:
        eOut.delete(0, 'end')
        eOut.insert(0, out)
        output = out

def log(log, arg = None):
    logs = ["Select folder containing all your sprites only",
            "Select one or more image files",
            "{} sprites added",
            "List cleared",
            "Sprites would {} aligned"]
    
    if isinstance(arg, int):
        logs[2] = logs[2].format(arg)
    if isinstance(arg, bool):
        if arg:
            logs[4] = logs[4].format("horizontally")
        else:
            logs[4] = logs[4].format("vertically")
    
    lLog.config(text = "-- {} --".format(logs[log]))

def make():
    testImg = Image.open(sprites[0])
    imgWidth = testImg.width
    imgHeight = testImg.height
    imgFormat = testImg.format
    del testImg
    hor = horz.get()
    output = eOut.get()

    img = Image.new('RGBA', (imgWidth * len(sprites)**hor, imgHeight * len(sprites)**int(not(hor)) ))
    co = 0
    if hor:
        for i in sprites:
            sprite = Image.open(i)
            img.paste(sprite, (co, 0))
            co += imgWidth
    else:
        for i in sprites:
            sprite = Image.open(i)
            img.paste(sprite, (0, co))
            co += imgHeight
    img.save(output)

## Main Window 
window = Tk()
window.title("SpriteSheet Maker")

mainFrame = Frame(master = window)
mainFrame.pack(fill = 'both', expand = 'true', padx = 10, pady = 10)

## Frame 1 - Source
frame1 = Frame(master = mainFrame)
frame1.pack(pady = 3)

src = None

rFolder = Radiobutton(master = frame1, text = "Folder", variable = src, value = True, command = selectFolder)
rFolder.pack(side = 'left')
rFolder.select()

rFiles = Radiobutton(master = frame1, text = "Files", variable = src, value = False, command = selectFiles)
rFiles.pack(side = 'right')

## Frame 2 - File Selection
frame2 = Frame(master = mainFrame)
frame2.pack(pady = 3)

lSrc = Label(master = frame2, text = "Source Folder: ")
lSrc.pack(side = 'left')


lSrcLoc = Label(master = frame2, width = 50, text = currDir, relief = 'groove')
lSrcLoc.pack(side = 'left')

bSrc = Button(master = frame2, text = "Browse", command = srcBrowseFolder)
bSrc.pack(side = 'left', padx = 10)

## Frame 3 - Files
frame3 = Frame(master = mainFrame)
frame3.pack(pady = 3)

lFiles = Label(master = frame3, text = "Sprites\nSelected: ")
lFiles.pack(side = 'left')

lbFiles = Listbox(master = frame3, width = 35)
lbFiles.pack(side = 'left')

sbFiles = Scrollbar(master = frame3)
sbFiles.pack(side = 'left', fill = 'y')

lbFiles.config(yscrollcommand = sbFiles.set)
sbFiles.config(command = lbFiles.yview)

bClear = Button(master = frame3, text = "Clear List", command = clearList, state = 'disabled')
bClear.pack(side = 'left')

## Frame 4 - Orientation
frame4 = Frame(master = mainFrame)
frame4.pack(pady = 3)

lOrien = Label(master = frame4, text = "Orientation: ")
lOrien.pack(side = 'left')

horz = BooleanVar()

rOrienH = Radiobutton(master = frame4, text = "Horizontal", variable = horz, value = True, command = lambda: log(4, True))
rOrienH.pack(side = 'left')
rOrienH.select()

rOrienV = Radiobutton(master = frame4, text = "Vertical", variable = horz, value = False, command = lambda: log(4, False))
rOrienV.pack(side = 'right')

## Frame 5 - Output
frame5 = Frame(master = mainFrame)
frame5.pack(pady = 3)

lOut = Label(master = frame5, text = "Output: ")
lOut.pack(side = 'left')

eOut = Entry(master = frame5, width = 55)
eOut.pack(side = 'left')
eOut.insert(0, output)

bOut = Button(master = frame5, text = "Browse", command = outBrowse)
bOut.pack(side = 'left', padx = 10)

## Area 6 - Log
lLog = Label(master = mainFrame, text = "--Log--")
lLog.pack(pady = 3)
log(0)

## Area 7 - Submit
bSubmit = Button(master = mainFrame, text = "Make", state = 'disabled', command = make)
bSubmit.pack(pady = 3)

window.mainloop()
