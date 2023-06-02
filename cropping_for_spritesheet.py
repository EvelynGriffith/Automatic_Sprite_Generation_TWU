"""This file will hopefully crop the image without the background into several images that can then be fed 
into a spritesheet creator."""

from PIL import Image
import numpy as np
# from rembg import remove
import easygui as eg
# from dotenv() import load_dotenv
# import cloudinary
import cloudinary.uploader
import cloudinary.api
import character_extraction
import cloudinary

pics = r'C:\Users\gforc\OneDrive\Desktop\rembg\*'

input = character_extraction.extracting(pics)

# Create an object, output_path and use easygui's file save dialog box to capture the file path and save it to the object
# output_path = eg.filesavebox(msg='Save file to..', default=r'C:\Users\gforc\OneDrive\Desktop\rembg\*')

# Create an object, input and use it to open and store the image via PIL's Image.open function.
new_input = Image.open(input)

new_input.show()

# image=np.array(new_input)

# x = image.shape[1]
# y = image.shape[0]

# print(x, y)


# box = ((2*x), (2*y), (2*(x + x)), (2*(y + y)))
# #(2*(x + x))

# img2 = new_input.crop(box)

# img2.save('C:\\Users\\gforc\\OneDrive\\Desktop\\rembg\\new_photo.png')
# img2.show()

"""Try to add if statements here to see if you can get it to crop based on what's in the scene?"""
#this will add gravity to the faces in the image and crop accordingly
CloudinaryImage(new_input).image(width=250, height=250, gravity="faces", crop="fill")

# this will add gravity to the central object in the image and crop accordingly.
# CloudinaryImage(new_input).image(width=200, height=300, gravity="auto", crop="fill")

