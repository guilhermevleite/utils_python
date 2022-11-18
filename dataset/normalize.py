"""
For some reason, some of my masks are annotated between 0-1 or 0-2,
and I need them with 0-255. This script does that.
"""


import numpy as np
import cv2 as cv
import argparse


def parse_args():
    args = argparse.ArgumentParser()

    args.add_argument('--input', type=str, required=True, 
                      default='poop.png',
                      help='Path to input image (Default: poop.png)')

    return args.parse_args()


def norm(img):
    print('Many classes', np.unique(img))
    while np.unique(img).size > 2:
        img = img / img.max()
    img = img / img.max()
    print('Single class', np.unique(img))

    return img * 255


def main():
    args = parse_args()
    
    img = cv.imread(args.input, 0)
    
    if np.unique(img).size <= 1:
        print('Image has only ONE class')
        exit()

    img = norm(img).astype('uint8')
    print('Normalized', np.unique(img), img.dtype)

    cv.imwrite(args.input, img)
    

if __name__=='__main__':
    main()
