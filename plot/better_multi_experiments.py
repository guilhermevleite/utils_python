import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
    df.insert(len(df.columns), 'experiment', exp_name, True)
    df.insert(len(df.columns), 'replica', replica, True)


if __name__ == "__main__":

    args = arg_parse()

    output_df = pd.DataFrame()

    for experiment in config['sub_strings']:
        print(f'Gathering information about {experiment}')
        replicates = Path(args.input_path).glob(f'{experiment}*')

        for idx, replica in enumerate(replicates):

            csv = pd.read_csv(Path(replica) / 'log.csv')
            output = csv[['epoch', 'val_dice']]
            print(len(output), len(output.columns))
            adapt_df(output, experiment, idx)
            print(len(output), len(output.columns))
            print()
            output_df = pd.concat([output_df, output])
            print('aapend', len(output_df))

    sns.set_theme(style="darkgrid")
    sns.lineplot(x='epoch', y='val_dice', hue='experiment', data=output_df)
    plt.ylim([0.85, 1.0])
    plt.show()

    # print(output_df)
    # output_df.to_csv('aqui.csv')
