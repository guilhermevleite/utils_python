import pandas as pd
import argparse
import numpy as np
from pathlib import Path
import  matplotlib.pyplot as plt
import seaborn as sns


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', type=str, required=True,
            help='Path to the UNEXT model folder.')

    return parser.parse_args()


def load_all_csv(csv_home_path: str, val_losses, val_ious, val_dices):

    print(csv_home_path, str(Path(csv_home_path).glob('*/*.csv')))
    paths = sorted(Path(csv_home_path).glob('*/*.csv'))
    print(paths)
    for idx, file in enumerate(paths):
        print('Loading', file)
        df = pd.read_csv(file)
        val_losses.append(df['val_loss'].to_numpy())
        val_ious.append(df['val_iou'].to_numpy())
        val_dices.append(df['val_dice'].to_numpy())


def plot_graphs(experiment_list, file_name):

    sns.set_theme()
    p = None
    for idx, experiment in enumerate(experiment_list):
        print(idx)
        p = sns.relplot(data=experiment, kind='line')
        plt.ylim((0, 1))
        plt.savefig('/home/leite/workspace/deep_learning/utils/{}_{}.png'.format(file_name, idx))


def main():
    args = arg_parse()

    val_losses = []
    val_ious = []
    val_dices = []

    load_all_csv(args.input, val_losses, val_ious, val_dices)

    print('Loaded csv:', len(val_losses))
    plot_graphs(val_losses, '1_isic_loss')
    # plot_graphs(val_dices, 'dice_isic')

    # plot_graphs(val_losses[:10], 'loss_busi')
    # plot_graphs(val_losses[10:], 'loss_isic')

    # plot_graphs(val_ious[:10], 'iou_busi')
    # plot_graphs(val_ious[10:], 'iou_isic')

if __name__ == "__main__":
    main()
