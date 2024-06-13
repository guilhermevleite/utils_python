import argparse
from pathlib import Path
import pandas as PD
import matplotlib.pyplot as PLT
import seaborn as SBN


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input_path', type=str, required=True,
                        help='Path to experiments folder.')

    return parser.parse_args()


def main():

    args = arg_parse()

    path = Path(args.input_path).glob('./*')
    # SBN.set_theme()
    exp_names = []
    df = None

    ## OO style of Matplot, uses pyplot just to create the figure
    fig, ax = PLT.subplots()

    for idx, experiment in enumerate(sorted(path)):
        csv_path = Path(experiment) / 'log.csv'

        if not experiment.is_dir():
            continue

        try:
            df = PD.read_csv(csv_path)
        except:
            print('Failed', experiment.name)
            continue

        ax.plot(df['val_dice'], label=experiment.name)

        # if idx == 2:
        #     break

    ax.set_xlabel('Epochs')
    ax.set_ylabel('Dice')
    ax.legend()

    PLT.xlim([0, 100])
    PLT.ylim([0.85, 1.0])
    PLT.savefig(Path(args.input_path) / 'Experiments.png')


if __name__ == '__main__':
    main()
