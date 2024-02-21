import argparse
from pathlib import Path
import numpy as NP
import pandas as PD
import matplotlib.pyplot as PLT
import seaborn as SB


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input_path', type=str, required=True,
                        help='Path to experiments instances folder.')
    parser.add_argument('-f', '--flag', type=bool, default=False,
                        help='Wether to print the mean graph (True), or each individual graph (False)')

    return parser.parse_args()


def main():

    args = arg_parse()

    folders = Path(args.input_path).glob('./*')

    aux_exp_list = []
    std_dev_values = []

    SB.set_theme()

    highest = -1
    idx = 0
    max = -1
    for idx, experiment in enumerate(sorted(folders)):

        if idx >= 3:
            continue

        csv_path = Path(experiment) / 'log.csv'

        experiment_dataframe = None
        try:
            experiment_dataframe = PD.read_csv(csv_path)
        except:
            print('Reading .csv failed', experiment.name)
            exit()

        dice_list = experiment_dataframe['val_dice'].values.tolist()
        aux_exp_list.append(dice_list[-1])
        if len(dice_list) > max:
            max = len(dice_list)

        print(dice_list[-1])


        if not args.flag:
            SB.lineplot(dice_list)

    print(f"Open {len(aux_exp_list)} experiments")

    average = NP.average(aux_exp_list, axis=0)
    std_d = NP.std(aux_exp_list)
    print(aux_exp_list, std_d)
    PLT.text(max//2, 0.5, f"Mean:{average:.3f}\nStd_d:{std_d:.3f}")


    if args.flag:
        for i in range(idx):
            print(i, aux_exp_list[i][highest])
            std_dev_values.append(aux_exp_list[i][highest])

        ax = SB.lineplot(average)
        print(f"Std_d {NP.std(std_dev_values):.6f}")
        PLT.text(highest-10, average[highest]-0.1, f'max[{highest}]: {average[highest]:.2f}\nstd_d: {NP.std(std_dev_values):.3f}')
        # PLT.text(99, average[99]-0.2, f'epoch[99]: {average[99]:.2f}')

    PLT.ylim(0,1.0)
    PLT.xlim(0,200)

    PLT.waitforbuttonpress()


main()
