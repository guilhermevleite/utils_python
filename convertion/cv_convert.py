"""
Convert image's format between OpenCV supported formats,
link to format list:

https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
"""


import argparse
from pathlib import Path
import cv2 as cv
import nd2


def parse_args():
    '''
    Setup argpase arguments
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('--input',
                         default=None,
                         help='Path to the input folder',
                         required=True)

    parser.add_argument('--output',
                         default=None,
                         help='Path to the output folder',
                         required=True)

    parser.add_argument('--suffix',
                         default='.png',
                         help='Output extension (Default: .png)')

    return parser.parse_args()


def create_out_folder(output_path: str):
    '''
    If output folder does not exists, create it
    '''
    p = Path(output_path)
    p.mkdir(parents=True, exist_ok=True)


def list_files(path: str) -> list:
    '''
    Setup the list of file names
    '''
    return [ x for x in Path(path).glob('*') if x.is_file() ]


def convert_cv2_formats(file_path, args):
    '''
    Converts image using OpenCV
    '''
    image = cv.imread(str(file_path))

    if image is None:
        print('ERROR: OpenCV image not loaded')
        exit()

    output_path = Path(args.output, file_path.name).with_suffix(args.suffix)
    print(output_path.name)
    cv.imwrite(str(output_path), image)


def convert_nd2_format(file_path, args):
    '''
    Converts .nd2 images
    '''
    image = nd2.imread(str(file_path))
    # image = cv.imread(str(file_path))

    if image is None:
        print('ERROR: ND2 image not loaded')
        exit()

    output_path = Path(args.output, file_path.name).with_suffix(args.suffix)
    print(output_path.name)
    cv.imwrite(str(output_path), image)


def convert_files(file_list: list, args):
    '''
    Converts the files in <img_list>,
    and saves them into <dest> folder
    '''
    for file in file_list:
        if file.suffix == '.nd2':
            convert_nd2_format(file, args)
        else:
            convert_cv2_formats(file, args)


def main():
    '''
    Main body
    '''
    args = parse_args()

    create_out_folder(args.output)

    file_list = list_files(args.input)

    convert_files(file_list, args)



if __name__ == "__main__":
    main()
