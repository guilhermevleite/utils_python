'''
Script to bulk rename files on datasets.
It takes the path to the files, and a pattern.
Right now it only removes the pattern from the filename, while renaming. Useful to remove _masks for instance.
'''


import os
import argparse


def arg_parse():

    parser = argparse.ArgumentParser()

    parser.add_argument('--input', type=str, required=True,
            help='Path to the images folder. (database/images/ OR database/masks/)')
    parser.add_argument('--pattern', type=str, default=None,
            help='String to be removed from the filename.')
    parser.add_argument('--numberfy', type=bool, default=False,
            help='Rename all files into sorted numbers. (001.png, 002.png, ..., 099.png)')

    return parser.parse_args()


def remove_pattern(path, f_list, pattern, debug=False):

    for f in f_list:

        new_name = f.replace(pattern, '')
        print(os.path.join(path, new_name))

        if not debug:
            os.rename(os.path.join(path, f),
                    os.path.join(path, new_name))


def numberfy(path, f_list, debug=False):
    ''' Rename files in f_list by numbered fashion.
    Assumes sorted list, and max of 1000 files.
        
        Parameters:
            path <str>: Path to the f_list folder
            f_list <List>: List of image files
            debug <Boolean>: Debug mode

        Return <None>
    '''
    
    i = 1
    for f in f_list:

        extension = f.split('.')[-1]
        new_name = '{:04d}.{}'.format(i, extension)

        print(f, new_name)

        if not debug:
            os.rename(os.path.join(path, f),
                    os.path.join(path, new_name))

        i += 1


def main():

    args = arg_parse()

    f_list = os.listdir(args.input)
    f_list.sort()

    if args.pattern != None:
        remove_pattern(args.input, f_list, args.pattern)

    if args.numberfy:
        numberfy(args.input, f_list)


if __name__ == '__main__':
    main()
