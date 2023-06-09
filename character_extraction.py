"""Extracts a character from an image and makes them a rig-able png, also gathers the new file from the folder and performs
pifpaf on it."""
from rembg import remove
from PIL import Image
import easygui as eg
import subprocess
import glob
import os
import cv2

# TODO: Tell Bryan that the files need to be png format when generated (maybe he can make that happen).
# TODO: make the grabbing of the generated file automatic.

# gathering the file and cutting out the background.
from rembg import remove
from PIL import Image
import easygui as eg


# create an object, input_path and use it to store the path and name of a file that we wish to remove the background from
input_path = eg.fileopenbox(msg='Choose a file', default=r'C:\Users\gforc\OneDrive\Desktop\rembg\*')

# Create an object, output_path and use easygui's file save dialog box to capture the file path and save it to the object
output_path = eg.filesavebox(msg='Save file to..', default=r'C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs\*')

# Create an object, input and use it to open and store the image via PIL's Image.open function.
input = Image.open(input_path)

# use rembg to remove the background from the image.
output = remove(input)

# save the ne image using the file path stored in output_path.
output.save(output_path)



# TODO: get it to take the most recently generated file. Right now it just takes a most recent file.
"""takes the most recent file in the folder (so the generated file)"""
list_of_images = glob.glob(r'C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs') # * means all if need specific format then *.csv
latest_image = max(list_of_images, key=os.path.getmtime)
print(latest_image)



"""converts the most recent png image to a jpg so pifpaf can process it."""
# TODO: convert the png images to .jpg for the pifpaf functions.
# img_png = cv2.imread(max((glob.glob(r'C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs')), key=os.path.getmtime))
# print(img_png)
folder = open(r'C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs')
# # TODO: get the below code to work.
for i in folder:
    # TODO: get this jpg to be able to be saved.
    # path = r"C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs\file.jpg"
    # assert os.path.isfile(path)
    # with open(path, "r") as f:
    #     pass
    im = Image.open(folder[i])
    rgb_im = im.convert('RGB')
    rgb_im.save()
    

#TODO: get the call to the terminal command to work.
# calling the command to use pifpaf in the terminal, so that it will run the program automatically.
command = r"python -m openpifpaf.predict C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs\jesus.png --checkpoint shufflenetv2k16-wholebody --line-width=3 --image-output"
subprocess.run(command, shell=True)
output_path = eg.filesavebox(msg='Save file to..', default=r'C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs\bodypart_cropped_image_folder')
command.save(output_path)
#TODO: Link bodypart_cropping.py to this file through a terminal run command?