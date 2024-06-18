import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as PLT
import seaborn as SBN


config = {}
config['sub_strings'] = [
    'ours__GPT-test_aug-none_GPTNet',
    'ours__GPT-test_aug-none_Unet'
]

def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input_path', type=str, required=True,
                        help='Path to experiments folder.')

    parser.add_argument('-o', '--output', dest='output_path', type=str, required=True,
                        help='Output path to save the results.')

    return parser.parse_args()


def adapt_df(df, exp_name, replica):
    df.insert(-1, 'experiment', exp_name, True)
    df.insert(-1, 'replica', replica, True)


if __name__ == "__main__":

    args = arg_parse()

    for experiment in config['sub_strings']:

        print(f'Gathering information about {experiment}')
        replicates = Path(args.input_path).glob(f'{experiment}*')
        result_list = []

        for idx, replica in enumerate(replicates):

            csv = pd.read_csv(Path(replica) / 'log.csv')
            output = csv[['epoch', 'val_dice']]
            adapt_df(csv, experiment, idx)
            result_list.append(output)

        print(len(result_list))
        print(result_list)
