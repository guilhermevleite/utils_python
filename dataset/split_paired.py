"""
This code exists on the sole purpose of splitting a pool of
paired data, like image|masks, into two pools, train and
validation, and also move those files into their new folders.

Assumptions: I assume that the images are in a folder called
images, and the masks are in a sibling folder called masks. The
same structured will be created in the output folder. I also
assume that both an image file and its associated mask have the
same file name.

--input ~/source/DB/origin/images/
--output ~/source/DB/train/images/

Assuming there are:
    ~/source/DB/train/masks/
    ~/source/DB/val/images/
    ~/source/DB/val/masks/
"""


import os
import argparse
import random
import shutil


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    parser.add_argument('--proportion', type=float, required=False)

    return parser.parse_args()


def split_file_list(file_list, proportion=0.2, debug=False):
    ''' Takes a list and splits into train and validation, based
    on proportion parameter. Returns two lists, with the file's
    names. '''

    # Output lists
    t_file_list = []
    v_file_list = []
    
    # Sort list before shuffling it
    file_list.sort()
    random.shuffle(file_list)

    # Size of each set
    n_v_files = int(len(file_list) * proportion)
    n_t_files = len(file_list) - n_v_files
    if debug:
        print('\tProportion:', proportion,
                '\n\t# Train files:', n_t_files,
                '\n\t# Val files:', n_v_files)

    # Assign each file to their list
    for i in range(n_v_files):
        v_file_list.append(file_list[i])

    for j in range(n_v_files, n_v_files+n_t_files):
        t_file_list.append(file_list[j])

    return (t_file_list, v_file_list)


def move_files(ori, dest, f_list, debug=False):
    ''' Move the files in list into the output folder. '''

    for f in f_list:
        print('Moving', os.path.join(ori, f), '\ninto:',
                os.path.join(dest, f), '\n')

        if not debug:
            os.rename(os.path.join(ori, f),
                    os.path.join(dest, f))

def main():

    args = arg_parse()
    
    file_pool = os.listdir(args.input)

    if args.proportion == None: args.proportion = 0.2

    train, val = split_file_list(file_pool, args.proportion,
            debug=True)
    print()

    # Train
    move_files(args.input,
            args.output,
            train,
            debug=False)
    move_files(args.input.replace('images', 'masks'),
            args.output.replace('images', 'masks'),
            train,
            debug=False)

    # Validation
    move_files(args.input,
            args.output.replace('train', 'val'),
            val,
            debug=False)
    move_files(args.input.replace('images', 'masks'),
            args.output.replace('images', 'masks').replace('train', 'val'),
            val,
            debug=False)


if __name__ == '__main__':
    main()
