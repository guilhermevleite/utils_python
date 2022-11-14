import os
import cv2 as cv
import numpy as np


path = '/home/leite/Workspace/deep_learning/db/ours/riboflavin_nov_21/72/'
output = '/home/leite/Workspace/deep_learning/db/ours/processed/nov_21/72/'

for file in os.listdir(path):
    img = cv.imread(path + file, 0)
    cv.resize(img, (224, 224))

    print(img.shape, np.min(img), np.max(img))
    file = file.replace('.tif', '.png')
    cv.imwrite(output+file, img)
