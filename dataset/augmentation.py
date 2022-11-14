import os
import cv2 as cv
import numpy as np
import albumentations as A
import matplotlib.pyplot as plt


IMG_DIR = '/home/leite/Workspace/deep_learning/db/sartorius/train/images/'
MSK_DIR = '/home/leite/Workspace/deep_learning/db/sartorius/train/masks/'


def bright_contrast(image, mask):
    transform = A.Compose([
        A.RandomBrightnessContrast(p=1.0)
        ])

    transformed = transform(image=image)
    aug_image = transformed["image"]

    return aug_image, mask


def rotate90(image, mask):
    transform = A.Compose([
        A.RandomRotate90(p=1.0)
        ])

    transformed = transform(image=image, mask=mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    return aug_image, aug_mask


def perspective(image, mask):
    transform = A.Compose([
        A.Perspective(keep_size=True, p=1.0)
        ])

    transformed = transform(image=image, mask=mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    return aug_image, aug_mask


def optical_distortion(image, mask):
    transform = A.Compose([
        A.OpticalDistortion(p=1.0)
        ])

    transformed = transform(image=image, mask=mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    return aug_image, aug_mask


def piece_affine(image, mask):
    transform = A.Compose([
        A.PiecewiseAffine(p=1.0)
        ])

    transformed = transform(image=image, mask=mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    return aug_image, aug_mask


def v_flip(image, mask):
    transform = A.Compose([
        A.VerticalFlip(p=1.0)
        ])

    transformed = transform(image=image, mask=mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    return aug_image, aug_mask


def h_flip(image, mask):
    transform = A.Compose([
        A.HorizontalFlip(p=1.0)
        ])

    transformed = transform(image=image, mask=mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    # aug_image = np.concatenate((image, aug_image), axis=1)
    # aug_mask = np.concatenate((mask, aug_mask), axis=1)
    # colation = np.concatenate((aug_image, aug_mask), axis=0)

    # print(aug_image.shape, aug_mask.shape)

    # plt.imshow(colation)
    # plt.show()

    return aug_image, aug_mask


def dummy(image, mask):
    transform = A.Compose([
        A.Affine(p=1.0)
        ])

    transformed = transform(image=image, mask=mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    aug_image = np.concatenate((image, aug_image), axis=1)
    aug_mask = np.concatenate((mask, aug_mask), axis=1)
    colation = np.concatenate((aug_image, aug_mask), axis=0)

    # print(aug_image.shape, aug_mask.shape)

    plt.imshow(colation)
    plt.show()

    return aug_image, aug_mask


def augment(image_file):
    aug_list = ['h_flip', 'v_flip', 'piecewise_affine', 'optical_distortion', 'perspective', 'rotate90', 'bright_contrast']
    aug_img = None
    aug_msk = None

    img = cv.imread(os.path.join(IMG_DIR, image_file), 0)
    msk = cv.imread(os.path.join(MSK_DIR, image_file), 0)

    img = cv.resize(img, (224,224))
    msk = cv.resize(msk, (224,224))

    for aug in aug_list:
        new_file_name = image_file.split('.')[0]

        if aug == 'h_flip':
            new_file_name = new_file_name + '_' + aug + '.png'
            aug_img, aug_msk = h_flip(img, msk)

        elif aug == 'v_flip':
            new_file_name = new_file_name + '_' + aug + '.png'
            aug_img, aug_msk = v_flip(img, msk)

        elif aug == 'piecewise_affine':
            new_file_name = new_file_name + '_' + aug + '.png'
            aug_img, aug_msk = piece_affine(img, msk)

        elif aug == 'optical_distortion':
            new_file_name = new_file_name + '_' + aug + '.png'
            aug_img, aug_msk = optical_distortion(img, msk)

        elif aug == 'perspective':
            new_file_name = new_file_name + '_' + aug + '.png'
            aug_img, aug_msk = perspective(img, msk)

        elif aug == 'rotate90':
            new_file_name = new_file_name + '_' + aug + '.png'
            aug_img, aug_msk = rotate90(img, msk)

        elif aug == 'bright_contrast':
            new_file_name = new_file_name + '_' + aug + '.png'
            aug_img, aug_msk = bright_contrast(img, msk)

        else:
            new_file_name = new_file_name + '_' + aug + '.png'
            aug_img, aug_msk = dummy(img, msk)

        # print(os.path.join(IMG_DIR + new_file_name))
        # print(os.path.join(MSK_DIR + new_file_name))
        print(new_file_name)

        cv.imwrite(os.path.join(IMG_DIR, new_file_name), aug_img)
        cv.imwrite(os.path.join(MSK_DIR, new_file_name), aug_msk)


def main():
    file_list = os.listdir(IMG_DIR)
    file_list.sort()

    for img in file_list:
        # print('bef:', len(file_list))
        augment(img)
        # print('aft:', len(file_list))

    return


main()
