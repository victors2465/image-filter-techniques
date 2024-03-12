'''

File name: cvlib.py 
Description: This script with functions to load, visualize and apply different transformations

Author: Victor Santiago Solis Garcia
Creation date: 03/12/2024

Usage example:  python3 test_image_filtering.py -i newcastle-beach.jpeg -f average -k 11 
                python3 test_image_filtering.py -i newcastle-beach.jpeg -f average
                python3 test_image_filtering.py -i newcastle-beach.jpeg -f MEDIAN 
-f options: median - average - gaussian

'''

import sys  
import cv2
import numpy as np

def read_image(path:str)->cv2:
    #Function to read an image
    #Parameters:    path(str): Path to the image
    #Returns:       img(cv2): Loaded cv2 image

    img = cv2.imread(path)
    if img is not None:
        print(f'The image was succesfully loaded')
        return img
    elif img is None:
        sys.exit('The image can not be loaded')

def visualize_image(title:str,img:cv2)->None:
    #Function to visualize an image
    #Parameters:    title(str): Title of the created window
    #               img(cv2): A cv2 image
    #Returns:       Nothing

    cv2.namedWindow(title,cv2.WINDOW_NORMAL)
    cv2.imshow(title,img)

def rotate_image(img:cv2,angle:np.cfloat=45)->cv2:
    #Function to rotate an image
    #Parameters:    angle(float): Angle of rotation, default value =45
    #               img(cv2): A cv2 image
    #Returns:       img_rotated(cv2)r: Rotated image.

    copy_image = img
    (h,w) = img.shape[:2]
    angle_Rotation = angle
    center = (w/2,h/2)
    matrix = cv2.getRotationMatrix2D(center,angle_Rotation,scale=1)
    img_rotated = cv2.warpAffine(copy_image,matrix,(w,h))
    return img_rotated

def translated_image(img:cv2,translation:np.intc=50)->cv2:
    #Function to rotate an image
    #Parameters:    translation(int): Number of pixels default value = 50 
    #               img(cv2): A cv2 image
    #Returns:       img_rotated(cv2)r: Translated image.

    copy_image = img
    (h,w) = img.shape[:2]
    M = np.float32([
        [1, 0, translation],
        [0, 1, 0]
    ])
    img_translatd = cv2.warpAffine(copy_image,M,(w,h))
    return img_translatd

def flip_image(img:cv2,flip_argument:int)->cv2:
    #Function to rotate an image
    #Parameters:    flip_argument(int): Flip argument
    #               img(cv2): A cv2 image
    #Returns:       img_reflected(cv2)r: Reflected image.
    if flip_argument not in (-1,0,1):
        raise ValueError('The flip argument must be -1,0 or 1')
    else:
        img_reflected = cv2.flip(img,flip_argument)
        return img_reflected
    
