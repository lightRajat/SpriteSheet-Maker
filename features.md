# Features

> A simple tool to combine all your sprites into a single sprite-sheet image, for game develpment.

## High Level Features

1. Option to output sprites of **multiple animations** into a single sprite-sheet image. Each animation would be put on a new line of images.

2. Option to **orient the animations** either *horizontally* or *vertically*.

## UI Features

1. Option to browse either via *Folder* radio-button, in which case a folder needs to be selected containing all the sprites; or via *Files* radio-button, in which case, all the sprites need to be individually selected.

2. Animations can be **added** with the *Add Animation* button, or **removed** with the *Remove Animation* button.

3. Sprites in the current animation will be always be **visible** in the *Sprites* listbox.

4. **Automatically scrolls down** the listboxes of animations and sprites if the list grows beyond visibility; also **adding scrollbars**.

5. Option to **de-select / remove** all the sprites in the current animation with the *Clear List* button.

6. Option to select a custom **output path**, along with a custom **output name**. When the app starts, automatically sets a default output in the same directory where the app lies, with the name *'spritesheet.png'*

7. A **responsive log** is available to give an active feedback to the user about the widgets and the status of processes.

## Inner Low Level Features

1. **App font** can be changed with a single variable.

2. All the widgets are aware and **in-sync** with other processes and change their own state accordingly- *normal* or *disabled*- to provide user-friendliness and prevent any bugs.

3. All the file-dialog boxes (***Browse* buttons**) open with the current directory.

4. *Browse Files* dialog box **shows only images**, preventing the selection of any other types of files.

5. **Automatically filters** images when selecting sprites through *Browse Folder* option.

6. **Automatically prevents duplicates**, in case a file has already been added.

7. The UI shows only the file-names, but the app stores full **file-paths internally**. This is to prevent app from considering two files with the same name residing in different locations, as duplicates.

8. The *Browse Ouptut* option only allows to save output with image formats.

9. Automatically **checks for different file formats**, in which case, the output won't be produced with a log message to the user.

10. Automatically **checks for invalid sprite dimensions**, in which case, the output won't be produced with a log message to the user.