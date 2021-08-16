from tkinter import *
from PIL import ImageTk, Image
import os

from tkinter import filedialog
root = Tk()

folder_walk = os.walk('images')
image_list = next(folder_walk)[2]
cur_image = image_list[0]
index = 0

my_image = ImageTk.PhotoImage(Image.open('images/' + cur_image))
my_label = Label(image=my_image)
my_label.grid(row=0, column = 0, columnspan = 3)
status = Label(root, text = "Image 1 of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = W)
status.grid(row = 4, column = 0, columnspan = 3, sticky = W+E)



def left_pressed(event):
    prevImage()

def right_pressed(event):
    nextImage()

root.bind("<Left>", left_pressed)
root.bind("<Right>", right_pressed)

def open_file():
    global index
    filename = filedialog.askopenfilename(title = "Select a file")
    openImage(filename)
    res = len(filename) - 1 - filename[::-1].index('/')
    filename = filename[res + 1: len(filename)]

    try:
        index = image_list.index(filename)
        status = Label(root, text="Image " + str(index + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
        status.grid(row=4, column=0, columnspan=3, sticky=W + E)
    except:
        status = Label(root, text="New image", bd=1, relief=SUNKEN,
                       anchor=W)
        status.grid(row=4, column=0, columnspan=3, sticky=W + E)






def openImage(image_file):
    global my_image
    global my_label

    my_image = ImageTk.PhotoImage(Image.open(image_file))
    my_label.grid_forget()
    my_label = Label(image=my_image)
    my_label.grid(row=0, column=0, columnspan=3)


def nextImage():
    global index
    global cur_image
    global my_label
    global my_image
    global status

    if index == len(image_list) - 1:
        index = 0
    else:
        index += 1
    cur_image = image_list[index]
    cur_image= 'images/' + cur_image
    openImage(cur_image)
    status = Label(root, text="Image " + str(index + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=4, column=0, columnspan=3, sticky=W + E)


def prevImage():
    global index
    global cur_image
    global my_label
    global my_image

    if index == 0:
        index = len(image_list) - 1
    else:
        index -= 1
    cur_image = image_list[index]
    cur_image = 'images/' + cur_image
    openImage(cur_image)
    status = Label(root, text="Image " + str(index + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=4, column=0, columnspan=3, sticky=W + E)

button_next = Button(root, text = ">>", command = nextImage)
button_prev = Button(root, text = "<<", command = prevImage)
button_exit = Button(root, text = "EXIT", command = root.quit)
button_open_file = Button(root, text = "Open image", command = open_file)
button_next.grid(row = 1, column = 2)
button_prev.grid(row = 1, column = 0)
button_exit.grid(row = 3, column = 1)
button_open_file.grid(row = 2, column = 1)

root.mainloop()