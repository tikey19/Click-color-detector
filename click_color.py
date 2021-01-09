# This is program that can be use to open an image, select one pixel and receive its color code.
from tkinter import *
from tkinter import filedialog
import sys
import cv2 as cv
from PIL import ImageTk, Image


# Function which opens a file explorer, selects an image and returns color code of selected pixel
def get_clr_code():
    # Opens file exp and save the file path in var 'filename'
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                          filetypes=(
                                              ('jpg files', '*.jpg'), ("png files", "*.png"), ("all files", "*.*")))

    # Opens new window
    top = Toplevel()
    my_image = ImageTk.PhotoImage(Image.open(filename))

    # Sets a new window dimensions same as image dimensions
    top.minsize(my_image.width(), my_image.height())

    # Displays selected image
    Label(top, image=my_image).pack()

    # Reads the selected image
    imCV = cv.imread(filename)

    def close_n_display(event):
        # The begining of the selected pixel's color code
        clr_code = '#'

        # Assign the list of BGR color code
        clr_list = imCV[event.x, event.y]

        # Inverts the BGR to RGB
        for i in range(2, -1, -1):
            # Gets the hex value of the code
            hex_value = hex(clr_list[i])

            # Makes a string of hex and formats hex value properly
            hex_value_formatted = str(hex_value).replace('0x', '')

            # Adds next value to our color code
            clr_code += hex_value_formatted

        # Displays our color code on main window
        txt.insert(INSERT, clr_code)
        txt.pack()

        # Closes new window
        top.destroy()

    # Detects the click and starts function 'close_n_display'
    top.bind("<Button-1>", close_n_display)

    # New window mainloop
    top.mainloop()
    return


# Main app window
root = Tk()

# App title
root.title('Color calculator')

# Main window dimensions
root.minsize(150, 100)

# File browser button
choose_file_b = Button(root, command=get_clr_code, text="Browse a file", width=10).pack()

# Exit button
exit_b = Button(root, command=sys.exit, text="Exit", width=10).pack()

# Display a result (color code)
txt = Text(root, width=7)

# Main window loop
root.mainloop()
