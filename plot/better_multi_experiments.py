import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


config = {}
config['sub_strings'] = [
    # 'manual_lacalle_manual_AUG_GPTNet',
    # 'manual_lacalle_manual_AUG_MultiResUnet',
    # 'manual_lacalle_manual_AUG_TransUnet',
    # 'manual_lacalle_manual_AUG_UnetPP',
    # 'swin_unet_lacalle_manual_AUG_SwinUnet',
    # 'manual_lacalle_manual_AUG_Unext',
    # 'manual_lacalle_manual_AUG_Unet',
    # 'spheroidj_lacalle_spheroidj_AUG_GPTNet',
    # 'spheroidj_lacalle_spheroidj_AUG_MultiResUnet',
    # 'spheroidj_lacalle_spheroidj_AUG_TransUnet',
    # 'spheroidj_lacalle_spheroidj_AUG_UnetPP',
    # 'swin_unet_lacalle_spheroidj_AUG_SwinUnet',
    # 'spheroidj_lacalle_spheroidj_AUG_Unext',
    # 'spheroidj_lacalle_spheroidj_AUG_Unet',
    'spheroid_ours_ALL_GPTNet',
    'spheroid_ours_ALL_MultiResUnet',
    'spheroid_ours_ALL_TransUnet',
    'spheroid_ours_ALL_UnetPP',
    'spheroid_ours_ALL_Unext',
    'spheroid_ours_ALL_Unet',
    'swin_unet_ours_ALL_SwinUnet',
]


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input_path', type=str, required=True,
                        help='Path to experiments folder.')

    parser.add_argument('-o', '--output', dest='output_path', type=str, required=True,
                        help='Output path to save the results.')

    return parser.parse_args()


def adapt_df(df, exp_name, replica):
    print(exp_name)
    exp_name = exp_name.split('_')[-1]
    df.insert(len(df.columns), 'experiment', exp_name, True)
    df.insert(len(df.columns), 'replica', replica, True)


if __name__ == "__main__":

    args = arg_parse()

    output_df = pd.DataFrame()

    for experiment in config['sub_strings']:
        print(f'Gathering information about {experiment}')
        replicates = Path(args.input_path).glob(f'{experiment}*')
        print(experiment + "*")

        for idx, replica in enumerate(replicates):

            csv = pd.read_csv(Path(replica) / 'log.csv')
            output = csv[['epoch', 'val_dice']]
            adapt_df(output, experiment, idx)
            print(len(output), len(output.columns))
            # print()
            output_df = pd.concat([output_df, output])
            # print('append', len(output_df))

    print(output_df.head)
    sns.set_theme(style="darkgrid")
    sns.lineplot(x='epoch', y='val_dice', hue='experiment', data=output_df)
    plt.ylim([0.85, 1.0])
    plt.show()

    # print(output_df)
    output_df.to_csv('aqui.csv')
