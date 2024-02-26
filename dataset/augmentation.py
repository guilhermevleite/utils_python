import argparse
from pathlib import Path
from tqdm import tqdm
import numpy as np
import cv2 as cv
import albumentations as A
import aug_list


def arg_parse() -> argparse.Namespace:
    '''
    Argument parser
    '''

    parser = argparse.ArgumentParser()

    parser.add_argument('--input', type=str, required=True,
                        help='Folder with all the input images.')
    parser.add_argument('--m_input', type=str, required=True,
                        help='Folder with all the corresponding mask images.')
    parser.add_argument('--output', type=str, required=True,
                        help='Folder to save all the augmented images. Original input is also saved.')
    parser.add_argument('--size', type=int, required=True,
                        help='Size of the output image. A size of 256 means an output of 256x256 pixels.')

    return parser.parse_args()


def load_image(img_path: Path) -> np.ndarray:
    '''
    Returns image loaded from img_path, also resizes to size. If
    load fails, returns black image.
    '''

    image = cv.imread(str(img_path))

    if image is None:
        image = np.zeros((128, 128), dtype='uint8')

    return image


def augmentation_pipeline(image: np.ndarray, mask: np.ndarray) -> tuple:
    '''
    Returns three lists. One with the original images and its
    augmentations, a second one with the original maks and its
    augmentations, and the third one with the suffixes to be used
    when saving these files.
    '''

    img_aug_lst = [image]
    msk_aug_lst = [mask]
    suffix_lst = ['ORI']

    # Mask AGNOSTIC augmentantions

    img = aug_list.bright_contrast(image)
    img_aug_lst.append(img)
    msk_aug_lst.append(mask)
    suffix_lst.append('BGT')

    img = aug_list.rdn_blur(image)
    img_aug_lst.append(img)
    msk_aug_lst.append(mask)
    suffix_lst.append('BLUR')

    # Mask SENSITIVE augmentations

    img, msk = aug_list.rotate90(image, mask)
    img_aug_lst.append(img)
    msk_aug_lst.append(msk)
    suffix_lst.append('90ROT')

    img, msk = aug_list.perspective(image, mask)
    img_aug_lst.append(img)
    msk_aug_lst.append(msk)
    suffix_lst.append('PERSP')

    img, msk = aug_list.optical_distortion(image, mask)
    img_aug_lst.append(img)
    msk_aug_lst.append(msk)
    suffix_lst.append('OPT')

    img, msk = aug_list.piece_affine(image, mask)
    img_aug_lst.append(img)
    msk_aug_lst.append(msk)
    suffix_lst.append('AFF')

    img, msk = aug_list.v_flip(image, mask)
    img_aug_lst.append(img)
    msk_aug_lst.append(msk)
    suffix_lst.append('VFLIP')

    img, msk = aug_list.h_flip(image, mask)
    img_aug_lst.append(img)
    msk_aug_lst.append(msk)
    suffix_lst.append('HFLIP')

    img, msk = aug_list.rdn_crop(image, mask)
    img_aug_lst.append(img)
    msk_aug_lst.append(msk)
    suffix_lst.append('CROP')

    return img_aug_lst, msk_aug_lst, suffix_lst


def save_images(folder: Path, ori_name: str, img_list: list, msk_list: list, out_size: int, suffix_lst: list) -> None:

    # Make sure output folders exists
    img_folder = folder / 'images'
    msk_folder = folder / 'masks/0'

    img_folder.mkdir(parents=True, exist_ok=True)
    msk_folder.mkdir(parents=True, exist_ok=True)

    for idx in range(len(img_list)):
        new_name = ori_name.split('.')[0] + '_' + suffix_lst[idx] + '.png'

        img_list[idx] = cv.resize(img_list[idx], (out_size, out_size))
        msk_list[idx] = cv.resize(msk_list[idx], (out_size, out_size))

        cv.imwrite(str(img_folder / new_name), img_list[idx])
        cv.imwrite(str(msk_folder / new_name), msk_list[idx])


def main():

    config = arg_parse()

    img_path_list = sorted(Path(config.input).glob('*'))
    mask_path_list = sorted(Path(config.m_input).glob('*'))

    for idx in tqdm(range(len(img_path_list))):

        image = load_image(img_path_list[idx])
        mask = load_image(mask_path_list[idx])

        img_aug_lst, msk_aug_lst, suffix_lst = augmentation_pipeline(image, mask)

        save_images(Path(config.output),
                    img_path_list[idx].name,
                    img_aug_lst,
                    msk_aug_lst,
                    config.size,
                    suffix_lst)


if __name__ == '__main__':
    main()
