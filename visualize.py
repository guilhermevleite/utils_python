import argparse
from pathlib import Path
import cv2 as cv
import numpy as np


COLOR = (255, 0, 0)
ALPHA = 0.4


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('--images', required=True)

    parser.add_argument('--masks', required=True)

    parser.add_argument('--output', required=True)

    return parser.parse_args()


def main():

    args = parse_args()

    img_folder = sorted(Path(args.images).glob('./*'))
    msk_folder = sorted(Path(args.masks).glob('./*'))

    folders = zip(img_folder, msk_folder)

    for img_path, msk_path in folders:

        img = cv.imread(str(img_path), 0)
        msk = cv.imread(str(msk_path), 0)

        cpy = np.copy(msk)
        cpy[cpy == 255] = 1

        cpy *= img

        assert img.shape[0] == msk.shape[0] and img.shape[1] == msk.shape[1]

        canvas = cv.hconcat([img, cpy, msk])
        output = Path(args.output) / str(img_path.name).replace('.tif', '.png')
        cv.imwrite(str(output), canvas)


# def main():
#
#     args = parse_args()
#
#     img_folder = sorted(Path(args.images).glob('./*'))
#     msk_folder = sorted(Path(args.masks).glob('./*'))
#
#     folders = zip(img_folder, msk_folder)
#
#     for img_path, msk_path in folders:
#
#         img = cv.imread(str(img_path))
#         msk = cv.imread(str(msk_path))
#
#         print(img_path.name, img.shape, msk.shape)
#
#         cpy = np.copy(msk)
#         test = cpy[:, :, 0] == 255
#         cpy[test] = COLOR
#
#         cpy = cv.addWeighted(img, 1.0, cpy, ALPHA, 0.0)
#         assert img.shape[0] == msk.shape[0] and img.shape[1] == msk.shape[1]
#
#         canvas = cv.hconcat([img, cpy, msk])
#         output = Path(args.output) / str(img_path.name).replace('.tif', '.png')
#         cv.imwrite(str(output), canvas)


if __name__ == '__main__':
    main()
