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

pics = r'C:\Users\gforc\OneDrive\Desktop\rembg\*'

input = character_extraction.extracting(pics)


# Create an object, output_path and use easygui's file save dialog box to capture the file path and save it to the object
# output_path = eg.filesavebox(msg='Save file to..', default=r'C:\Users\gforc\OneDrive\Desktop\rembg\*')

# Create an object, input and use it to open and store the image via PIL's Image.open function.
new_input = Image.open(input)

input.show()

image=np.array(new_input)

x = image.shape[1]
y = image.shape[0]

print(x, y)


box = ((x/2),x,(y/2),y)

img2 = new_input.crop(box)

img2.save('img_cropped_test.png')
img2.show()

# # Focus on the model in a portrait crop.

# CloudinaryImage("docs/model.jpg").image(gravity="person", height=600, width=450, crop="fill")

# # Detect the face for a thumbnail crop.

# CloudinaryImage("docs/model.jpg").image(gravity="face", height=250, width=250, crop="thumb")

# # Crop to a banner, automatically focusing on a region of interest.

# CloudinaryImage("docs/model.jpg").image(gravity="auto", height=150, width=600, crop="fill")
