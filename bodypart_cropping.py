"""This file will hopefully be able to take the body positions from pifpaf and use the numbers in the Constants.py file to crop the image
based on the body parts that need to be harvested for the spritesheet."""

# import copy
# import numpy
# import argparse

# import torch
import numpy as np

# import openpifpaf
import os
from PIL import Image
import easygui as eg
# from openpifpaf.plugins.coco import CocoDataset as Coco
# from .wholebody_metric import WholebodyMetric
# from .constants import (
#     COCO_CATEGORIES,
#     WHOLEBODY_KEYPOINTS,
#     WHOLEBODY_SKELETON,
#     WHOLEBODY_SIGMAS,
#     WHOLEBODY_SCORE_WEIGHTS,
#     WHOLEBODY_STANDING_POSE,
#     HFLIP,
#     training_weights_local_centrality
# )


body_kps = [
    'nose',            # 1
    'left_eye',        # 2
    'right_eye',       # 3
    'left_ear',        # 4
    'right_ear',       # 5
    'left_shoulder',   # 6
    'right_shoulder',  # 7
    'left_elbow',      # 8
    'right_elbow',     # 9
    'left_wrist',      # 10
    'right_wrist',     # 11
    'left_hip',        # 12
    'right_hip',       # 13
    'left_knee',       # 14
    'right_knee',      # 15
    'left_ankle',      # 16
    'right_ankle', ]     # 17

foot_kps = [
    'left_big_toe',    # 18
    'left_small_toe',  # 19
    'left_heel',       # 20
    'right_big_toe',   # 21
    'right_small_toe',  # 22
    'right_heel', ]     # 23

face_kps = ['f_' + str(x) for x in range(24, 92)]
lefth_kps = ['lh_' + str(x) for x in range(92, 113)]
righth_kps = ['rh_' + str(x) for x in range(113, 134)]

WHOLEBODY_KEYPOINTS = body_kps + foot_kps + face_kps + lefth_kps + righth_kps

SCALE_FACE = 1.05

body_pose = np.array([
    [0.0, 9.3, 2.0],    # 'nose',                         # 1
    [-0.35 * SCALE_FACE, 9.7, 2.0],  # 'left_eye',        # 2
    [0.35 * SCALE_FACE, 9.7, 2.0],   # 'right_eye',       # 3
    [-0.7 * SCALE_FACE, 9.5, 2.0],   # 'left_ear',        # 4
    [0.7 * SCALE_FACE, 9.5, 2.0],    # 'right_ear',       # 5
    [-1.4, 8.0, 2.0],   # 'left_shoulder',                # 6
    [1.4, 8.0, 2.0],    # 'right_shoulder',               # 7
    [-1.75 - 0.4, 6.2 + 0.2, 2.0],  # 'left_elbow',      # 8
    [1.75 + 0.4, 6.2 + 0.2, 2.0],   # 'right_elbow',     # 9
    [-1.75 - 0.5, 4.2 + 0.5, 2.0],  # 'left_wrist',      # 10
    [1.75 + 0.5, 4.2 + 0.5, 2.0],   # 'right_wrist',     # 11
    [-1.26, 4.0, 2.0],  # 'left_hip',        # 12
    [1.26, 4.0, 2.0],   # 'right_hip',       # 13
    [-1.4, 2.0, 2.0],   # 'left_knee',       # 14
    [1.4, 2.0, 2.0],    # 'right_knee',      # 15
    [-1.4, 0.0, 2.0],   # 'left_ankle',      # 16
    [1.4, 0.0, 2.0], ])    # 'right_ankle',     # 17

"""This is trying to make a folder generate automatically so that I have a place to put the cropped images."""
# Note: It generates the folder properly.
# TODO: How are you going to get a new folder to generate with a different knowable name every time?
newpath = r'C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs\bodypart_cropped_image_folder' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Opens a image in RGB mode
im = Image.open(r"C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs\jesus_nobk.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
# left = [-1.75 - 0.5, 4.2 + 0.5, 2.0] #<-- attempting to use bodypt recognition to identify cropping path.
#TODO: You may have to figure out how to get the general area of the body part that you're trying to crop based on these coordinates
# how could you do this mathematically speaking???
left = 100
top = height / 4
right = 164
bottom = 3 * height / 4
 
# Cropped image of above dimension
output_path = eg.filesavebox(msg='Save file to..', default=r'C:\Users\gforc\Automatic_Sprite_Generation_TWU\openpifpaf_TWU\docs\bodypart_cropped_image_folder\new_image.png')
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
# Shows the image in image viewer
im1.show()
im1.save(output_path)
