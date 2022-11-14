import os
import cv2 as cv
import numpy as np
import nd2


ori = '/home/leite/Workspace/deep_learning/db/lacalle/BN2S_old/images/Experiment0/'
dest = '/home/leite/Workspace/deep_learning/db/lacalle/BN2S/train/images/'


f_list = os.listdir(ori)
f_list.sort()

for file in f_list:

    img = nd2.imread(ori+file)
    img = cv.resize(img, (224, 224))
    print(img.shape, img.min(), img.max())

    new_name = file.replace('.nd2', '.png')
    cv.imwrite(dest+new_name, img)
