'''

File name: test_image_filtering.py 
Description: This script performs filtering image

Author: Victor Santiago Solis Garcia
Creation date: 03/12/2024

Usage example:  python3 test_image_filtering.py -i newcastle-beach.jpeg -f average -k 11 
                python3 test_image_filtering.py -i newcastle-beach.jpeg -f average
                python3 test_image_filtering.py -i newcastle-beach.jpeg -f MEDIAN 
-f options: median - average - gaussian

'''

import argparse
import cv2
import numpy as np

from modules import cvlib as cvl

def parser_user_data()->argparse:
    #Function to input the image, filter and the kernel size(optional), 
    #returns an argparse object 
    parser = argparse.ArgumentParser()

    parser.add_argument('-i',
                        required=True,
                        type=str,
                        help='Image to apply the filter')
    
    parser.add_argument('-f',
                        required=True,
                        type=str,
                        help='Filter, could be median,average or gaussian')
    
    parser.add_argument('-k',
                        type=int,
                        help='Kernel size',
                        default=5)
    
    args = parser.parse_args()
    
    return args

def median_filter(img:cv2,kernel:np.intc=3)->cv2:
    #Function to apply a median filter to an image, accept a cv2 image, 
    #and an integer for the kernel size and returns the filtered image.
    #The function verify if the kernel size is an odd.

    assert kernel%2 == 1, "Filter size must be an odd"

    median_image = cv2.medianBlur(img,kernel)
    return median_image


def average_filter(img:cv2,kernel:np.intc=3)->cv2:
    #Function to apply a average filter to an image, accept a cv2 image, 
    #and an integer for the kernel size and returns the filtered image
    #The function verify if the kernel size is an odd.

    assert kernel%2 == 1, "Filter size must be an odd"

    average_image = cv2.blur(img,(kernel,kernel))
    return average_image

def gaussian_filter(img:cv2,kernel:np.intc=3)->cv2:
    #Function to apply a gaussian filter to an image, accept a cv2 image, 
    #and an integer for the kernel size and returns the filtered image
    #The function verify if the kernel size is an odd.
    assert kernel%2 == 1, "Filter size must be an odd"

    gaussian_image = cv2.GaussianBlur(img,(kernel,kernel),0)
    return gaussian_image

def apply_filter(filter_name:str,
                 img:cv2,
                 kernel:np.intc=11)->cv2:
    #The apply_filter function receives an string filter name, a cv2 image 
    #and integer for the kernel size.
    #The function verify if the kernel size is an odd.
    #The function returns the filtered image 
    assert kernel%2 == 1, "Filter size must be an odd"

    match filter_name.lower():
        case "average":
            filtered_image=average_filter(img,kernel)
            print(f'Average filter applied')
        case "median":
            filtered_image=median_filter(img,kernel)
            print(f'Median filter applied')
        case "gaussian":
            filtered_image=gaussian_filter(img,kernel)
            print(f'Gaussian filter applied')
    return filtered_image

def close_windows()->None:
    #Function to close the windows created
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def run_pipeline()->None:
    #User input
    args = parser_user_data()
    #Load image
    img = cvl.read_image(args.i)
    #Kernel size
    print(f'Kernel size {args.k}')
    #Filter
    image_filtered = apply_filter(args.f,img,args.k)
    #show original and filtered image
    cvl.visualize_image(f'{args.f} filter',image_filtered)
    cvl.visualize_image("Original image",img)
    close_windows()

if __name__ == '__main__':
    run_pipeline()

    