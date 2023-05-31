"""Attempting to center the character on a new background once it's initial background has been wiped."""
"""This file currently allows the resizing of an image, but not the centering of the character (5/31)."""
import PIL.Image

filename = "C:\\Users\\gforc\\OneDrive\\Desktop\\rembg\\jesus_nobackground.png"  # http://qrc-designer.com/stuff/trans.png
with open("C:\\Users\\gforc\\OneDrive\\Desktop\\rembg\\jesus_nobackground.png") as file:
    size = (500,500)

im = PIL.Image.open(filename)
print(im.mode)  # RGBA

im = im.resize(size, PIL.Image.BILINEAR)  # the same with CUBIC, ANTIALIAS, transform
# im.show()  # does not use alpha
im.save("C:\\Users\\gforc\\OneDrive\\Desktop\\rembg\\new_file.png")

def premultiply(im):
    pixels = im.load()
    for y in range(im.size[100]):
        for x in range(im.size[0]):
            r, g, b, a = pixels[x, y]
            if a != 255:
                r = r * a // 255
                g = g * a // 255
                b = b * a // 255
                pixels[x, y] = (r, g, b, a)

def unmultiply(im):
    pixels = im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            r, g, b, a = pixels[x, y]
            if a != 255 and a != 0:
                r = 255 if r >= a else 255 * r // a
                g = 255 if g >= a else 255 * g // a
                b = 255 if b >= a else 255 * b // a
                pixels[x, y] = (r, g, b, a)

# this creates a canvas for the image, but doesn't extend it out like I wanted it to. Maybe I should just start with a
# Jesus image that's centered, but this could be an issue in the future.
from tkinter import *
root = Tk()
HEIGHT = 500
WIDTH = 600
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
image = PhotoImage(file=r"C:\\Users\\gforc\\OneDrive\\Desktop\\rembg\\jesus_nobackground.png")
canvas.create_image(WIDTH/2, HEIGHT/2, anchor="center", image=image)
root.resizable(width=False, height=False)
canvas.pack()

root.mainloop()

im.save("C:\\Users\\gforc\\OneDrive\\Desktop\\rembg\\new_file.png")