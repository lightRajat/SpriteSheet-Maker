from tkinter import Tk, Frame, Radiobutton, BooleanVar, Label, Entry, Button, Scrollbar, Listbox, filedialog, font
from os import listdir, getcwd
from PIL import Image

horz = None # True (later in code)
sprites = [[]]
currAnim = 1
currDir = getcwd()
output = currDir + "\spritesheet.png"
appFont = ("Comic Sans MS", 16)

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
        updateFiles(["{}/{}".format(folder, i) for i in listdir(folder) if i[i.rfind('.'):] in ('.png', '.jpg', '.jpeg')])

def srcBrowseFiles():
    files = filedialog.askopenfilenames(title = "Select one or more sprites", filetypes = (("Image Files", '*.jpg *.jpeg'), ("Image Files", '*.png')), initialdir = currDir)
    if files:
        updateFiles(files)

def updateFiles(files):
    global sprites
    x = 0
    for i in files:
        if i not in sprites[-1]:
            x += 1
            sprites[-1].append(i)
            lbSprites.insert('end', extractNames(i))
            bClear['state'] = 'normal'
            bSubmit['state'] = 'normal'
            bAddAnim['state'] = 'normal'
    lbSprites.see('end')
    log(2, x)

def extractNames(path):
    return path[path.rfind('/') + 1:]

def updateSpritesList():
    for i in sprites[-1]:
        lbSprites.insert('end', extractNames(i))

def addAnim():
    sprites.append([])
    global currAnim
    currAnim += 1
    lbAnim.insert('end', "Animation {}".format(currAnim))
    lbAnim.see('end')
    bRemAnim['state'] = 'normal'
    lbSprites.delete(0, 'end')
    bClear['state'] = 'disabled'
    bSubmit['state'] = 'disabled'
    bAddAnim['state'] = 'disabled'
    log(8)

def remAnim():
    global currAnim
    currAnim -= 1
    sprites.pop()
    lbAnim.delete('end')
    lbSprites.delete(0, 'end')
    updateSpritesList()
    bClear['state'] = 'normal'
    bSubmit['state'] = 'normal'
    bAddAnim['state'] = 'normal'

    if len(sprites) == 1:
        bRemAnim['state'] = 'disabled'
    log(9)

def clearList():
    sprites[-1].clear()
    lbSprites.delete(0, 'end')
    bClear.config(state = 'disabled')
    bSubmit.config(state = 'disabled')
    bAddAnim['state'] = 'disabled'
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
            "Sprites would {} aligned",
            "Done",
            "Can't process sprites of different formats",
            "Can't process sprites of disfferent sizes",
            "New empty animation added",
            "Last animation removed"]
    
    if isinstance(arg, int):
        logs[2] = logs[2].format(arg)
    if isinstance(arg, bool):
        if arg:
            logs[4] = logs[4].format("horizontally")
        else:
            logs[4] = logs[4].format("vertically")
    
    lLog.config(text = "-- {} --".format(logs[log]))

#### new feature
##
##def make():
##    hor = horz.get()
##    output = eOut.get()
##
##    img = Image.new('RGBA', (sprites[0].width * len(sprites)**hor, sprites[0].height * len(sprites)**int(not(hor)) ))
##    co = 0
##    if hor:
##        for sprite in sprites:
##            img.paste(sprite, (co, 0))
##            co += sprites[0].width
##    else:
##        for sprite in sprites:
##            img.paste(sprite, (0, co))
##            co += sprites[0].height
##    img.save(output)
##    log(5)
##
#### new feature

def make():
    # check if all images have same format
    sprites[0] = Image.open(sprites[0])
    for i in range(1, len(sprites)):
        sprites[i] = Image.open(sprites[i])
        if sprites[i].format != sprites[0].format:
            clearList()
            log(6)
            break
    else:
        # check if all images have same size
        for i in range(1, len(sprites)):
            if sprites[i].height != sprites[0].height or sprites[i].width != sprites[0].width:
                clearList()
                log(7)
                break
        else:
            # make
            hor = horz.get()
            output = eOut.get()

            img = Image.new('RGBA', (sprites[0].width * len(sprites)**hor, sprites[0].height * len(sprites)**int(not(hor)) ))
            co = 0
            if hor:
                for sprite in sprites:
                    img.paste(sprite, (co, 0))
                    co += sprites[0].width
            else:
                for sprite in sprites:
                    img.paste(sprite, (0, co))
                    co += sprites[0].height
            img.save(output)
            log(5)

## Main Window, outer frame & default font
window = Tk()
window.title("SpriteSheet Maker")

mainFrame = Frame(master = window)
mainFrame.pack(fill = 'both', expand = 'true', padx = 10, pady = 10)

font.nametofont("TkDefaultFont").configure(family = appFont[0], size = appFont[1])

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

### Frame 3a
frame3a = Frame(master = frame3)
frame3a.pack(side = 'left', padx = 5)

bAddAnim = Button(master = frame3a, text = "Add\nAnimation", state = 'disabled', command = addAnim)
bAddAnim.pack(pady = 5)

bRemAnim = Button(master = frame3a, text = "Remove\nAnimation", state = 'disabled', command = remAnim)
bRemAnim.pack(pady = 5)

### Frame 3b
frame3b = Frame(master = frame3)
frame3b.pack(side = 'left', padx = 5)

lAnim = Label(master = frame3b, text = "Animations")
lAnim.grid(row = 0, column = 0)

lSprites = Label(master = frame3b, text = "Sprites")
lSprites.grid(row = 0, column = 1)

#### Frame3ba
frame3ba = Frame(master = frame3b)
frame3ba.grid(row = 1, column = 0)

lbAnim = Listbox(master = frame3ba)
lbAnim.pack(side = 'left')
lbAnim.insert(0, "Animation 1")

sbAnim = Scrollbar(master = frame3ba)
sbAnim.pack(side = 'left', fill = 'y')

lbAnim.config(yscrollcommand = sbAnim.set)
sbAnim.config(command = lbAnim.yview)

#### Frame3bb
frame3bb = Frame(master = frame3b)
frame3bb.grid(row = 1, column = 1)

lbSprites = Listbox(master = frame3bb)
lbSprites.pack(side = 'left')

sbSprites = Scrollbar(master = frame3bb)
sbSprites.pack(side = 'left', fill = 'y')

lbSprites.config(yscrollcommand = sbSprites.set)
sbSprites.config(command = lbSprites.yview)

### Frame 3c
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
