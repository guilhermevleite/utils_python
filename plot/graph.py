"""
Script to load the training log.csv and plot the metrics

TODO make this script more general
"""

import argparse
from pathlib import Path
import pandas as PD
import seaborn as SBN
import  matplotlib.pyplot as plt


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--csv', type=str, required=True,
            help='Path to the .csv log')

    parser.add_argument('--out', type=str, required=True,
            help='Output plot folder')

    parser.add_argument('--experiment', type=str, required=False,
                        default='', help='Experiment name')

    return parser.parse_args()


def load_csv(file_path: str):
    df = None

    try:
        df = PD.read_csv(file_path)
    except:
        print('Could not read CSV file')
        exit()

    return df


def plot_line_graph(csv, train, val, args):
    SBN.set_theme()
    plot = None

    plot = SBN.relplot(
            data=(csv[train], csv[val]),
            kind='line',
            dashes=False,
            legend=False)
    plot.set(title=args.experiment, xlabel='Epoch', ylabel=train)
    plt.legend(labels=['Train', 'Validation'])
    plt.ylim((0, 1))

    file_name = args.experiment +'_'+ train + '.png'
    plt.savefig(Path(args.out, file_name), bbox_inches='tight')


def main():
    args = arg_parse()

    csv = load_csv(args.csv)

    plot_line_graph(csv, 'loss', 'val_loss', args)
    plot_line_graph(csv, 'iou', 'val_iou', args)


if __name__ == "__main__":
    main()
