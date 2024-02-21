import albumentations as A


# Mask AGNOSTIC augmentantions

def bright_contrast(image):
    transform = A.Compose([
        A.RandomBrightnessContrast(p=1.0)
        ])

    transformed = transform(image=image)
    aug_image = transformed["image"]

    return aug_image


# Mask SENSITIVE augmentations

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
