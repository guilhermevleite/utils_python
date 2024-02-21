import argparse
from pathlib import Path

from roifile import ImagejRoi
import numpy as NP
import cv2 as CV


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', '-i', required=True,
                        help='Path to input FOLDER')

    parser.add_argument('--output', '-o', required=True,
                        help='Path to output folder')

    parser.add_argument('--size', type=int, default=1600, required=False,
                        help='Desired image output size, [size x size]. \
                                Default: 1600x1600')

    return parser.parse_args()


def main():

    args = parse_args()

    roi_list = Path(args.input).glob('./*.roi')

    for idx, file in enumerate(sorted(roi_list)):

        roi = ImagejRoi.fromfile(file)
        coord_list = NP.array(roi.integer_coordinates, dtype=NP.int32)

        ''' ImageJ saves the coordinates from the top and left margin of the
        image, so we need to offset the coordinates '''
        temp_list = [[x + roi.left, y + roi.top]
                     for x, y in roi.integer_coordinates]

        # Convert to int32, otherwise will raise error
        coord_list = NP.array(temp_list, dtype=NP.int32)

        blank_img = NP.zeros((args.size, args.size), NP.uint8)

        # blank_img = CV.polylines(blank_img, [coord_list], True, (255, 255, 255))
        blank_img = CV.fillPoly(blank_img, [coord_list], color=(255, 255, 255))

        print(idx, file.name, coord_list.shape)

        new_name = (file.name).replace('.roi', '.png')
        output = Path(args.output) / new_name
        CV.imwrite(str(output), blank_img)


if __name__ == '__main__':
    main()
