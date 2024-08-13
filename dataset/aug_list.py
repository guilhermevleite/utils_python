import albumentations as A
import cv2 as cv


# Patching image

# TODO : Currently only does 4 patches
def patching(image, mask):

    img_tuple_lst = []
    height, width, _ = image.shape

    # north west
    tmp_img = image[:height//2, :width//2]
    tmp_msk = mask[:height//2, :width//2]

    tmp_img = cv.resize(tmp_img, (height//2, width//2))
    tmp_msk = cv.resize(tmp_msk, (height//2, width//2))

    img_tuple_lst.append((tmp_img, tmp_msk))

    # north east
    tmp_img = image[:height//2, width//2:]
    tmp_msk = mask[:height//2, width//2:]

    tmp_img = cv.resize(tmp_img, (height//2, width//2))
    tmp_msk = cv.resize(tmp_msk, (height//2, width//2))

    img_tuple_lst.append((tmp_img, tmp_msk))

    # south west
    tmp_img = image[height//2:, :width//2]
    tmp_msk = mask[height//2:, :width//2]

    tmp_img = cv.resize(tmp_img, (height//2, width//2))
    tmp_msk = cv.resize(tmp_msk, (height//2, width//2))

    img_tuple_lst.append((tmp_img, tmp_msk))

    # south east
    tmp_img = image[height//2:, width//2:]
    tmp_msk = mask[height//2:, width//2:]

    tmp_img = cv.resize(tmp_img, (height//2, width//2))
    tmp_msk = cv.resize(tmp_msk, (height//2, width//2))

    img_tuple_lst.append((tmp_img, tmp_msk))

    return img_tuple_lst

# Mask AGNOSTIC augmentantions

def bright_contrast(image):
    transform = A.Compose([
        A.RandomBrightnessContrast(p=1.0)
        ])

    transformed = transform(image=image)
    aug_image = transformed["image"]

    return aug_image


def rdn_blur(image):
    transform = A.Compose([
        ])

    transformed = transform(image=image)
    aug_image = transformed["image"]

    return aug_image


# Mask SENSITIVE augmentations

def rotate90(image, mask):
    transform = A.Compose([
        A.RandomRotate90(p=1.0)
        ])

    _image = cv.resize(image, (SIZE, SIZE))
    _mask = cv.resize(mask, (SIZE, SIZE))

    transformed = transform(image=_image, mask=_mask)
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
    _image = cv.resize(image, (SIZE, SIZE))
    _mask = cv.resize(mask, (SIZE, SIZE))

    transformed = transform(image=_image, mask=_mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    return aug_image, aug_mask


def rdn_crop(image, mask):
    transform = A.Compose([
        A.RandomCrop(width=SIZE, height=SIZE)
        ])

    _image = cv.resize(image, (SIZE, SIZE))
    _mask = cv.resize(mask, (SIZE, SIZE))

    transformed = transform(image=_image, mask=_mask)
    aug_image = transformed["image"]
    aug_mask = transformed["mask"]

    return aug_image, aug_mask
