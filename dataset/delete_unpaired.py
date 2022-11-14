import os
import argparse
from pathlib import Path


def arg_parse():

    parser = argparse.ArgumentParser()

    parser.add_argument('--input', type=str, required=True,
            help='Path to the images folder.')
    parser.add_argument('--pair', type=str, required=True,
            help='Path to the paired images.')

    return parser.parse_args()


def remove_unpaired(path, l_one, l_two, debug=False):

    candidate = []
    for f in l_one:
        candidate = [ i for i in l_two if f.name in i.name ]
        if len(candidate) == 0:
            print(f.name)
        if not debug and len(candidate) == 0:
            Path.unlink(f)


def main():

    args = arg_parse()

    i_list = list(sorted(Path(args.input).glob('*')))
    p_list = list(sorted(Path(args.pair).glob('*')))

    if len(i_list) > len(p_list):
        print('First -> Paired')
        remove_unpaired(args.input, i_list, p_list)
    else:
        print('Paired -> First')
        remove_unpaired(args.pair, p_list, i_list)



if __name__ == '__main__':
    main()
