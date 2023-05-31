"""Extracts a character from an image and makes them a rig-able png."""
from rembg import remove
from PIL import Image
import easygui as eg

def extracting(input_path):
# create an object, input_path and use it to store the path and name of a file that we wish to remove the background from
    input_path = eg.fileopenbox(msg='Choose a file', default=r'C:\Users\gforc\OneDrive\Desktop\rembg\*')

    # Create an object, output_path and use easygui's file save dialog box to capture the file path and save it to the object
    output_path = eg.filesavebox(msg='Save file to..', default=r'C:\Users\gforc\OneDrive\Desktop\rembg\*')

    # Create an object, input and use it to open and store the image via PIL's Image.open function.
    input = Image.open(input_path)

    # use rembg to remove the background from the image.
    output = remove(input)

    # save the ne image using the file path stored in output_path.
    outputting = output.save(output_path)
    return outputting