import os
import cv2 as cv
import numpy as np
from tqdm import tqdm


def check_mask_range(file_name, img):
    ''' Checks whether the mask has any value other than 0,1 '''
    unique_list = np.unique(img)
    print(unique_list, file_name)


def fix_mask_range(img):
    ''' Changes any value above 1 to 1 '''
    for row in range(len(img)):
        for column in range(len(img[0])):
            if img[row][column] > 1:
                img[row][column] = 1

    return img


def main():
    mask_path = '/home/leite/Workspace/deep_learning/db/sartorius/train/images/'
    file_list = os.listdir(mask_path)

    for file in tqdm(file_list):
        img = cv.imread(os.path.join(mask_path, file), 0)
        check_mask_range(img, file)
        # img = fix_mask_range(img)
        # cv.imwrite(os.path.join(mask_path, file), img)


main()
