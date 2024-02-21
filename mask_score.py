import argparse
from pathlib import Path
import numpy as np
import cv2 as CV2
from sklearn import metrics


# img1 = CV2.imread('/home/leite/workspace/deep_learning/datasets/segmentation/ours_filtered/masks/0/G007N_48.png', 0)
# img2 = CV2.imread('/home/leite/workspace/deep_learning/datasets/segmentation/ours_filtered/masks/0/H005B_96.png', 0)

# img1 = CV2.imread('/home/leite/workspace/deep_learning/datasets/segmentation/ours_filtered/masks/0/G007N_48.png', 0)
# img2 = CV2.imread('/home/leite/workspace/deep_learning/datasets/segmentation/ours_filtered/masks/0/H005B_96.png', 0)
#
# print(np.max(img1), np.max(img2))
#
# img1[img1 > 1] = 1
# img2[img2 > 1] = 1
#
# print(np.max(img1), np.max(img2))
#
# print(img1.shape, img2.shape)
#
# score = metrics.jaccard_score(img1, img2, average='micro')
#
# print(score)


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-gt', '--ground', dest='gt_path', type=str, required=True,
                      help='Path to ground truth images folder')

    parser.add_argument('-pd', '--pred', dest='pred_path', type=str, required=True,
                      help='Path to prediction images folder')

    return parser.parse_args()


def evaluate(img1, img2):

    img1[img1 > 1] = 1
    img2[img2 > 1] = 1

    score = metrics.jaccard_score(img1, img2, average='micro')

    return score


def main():
    args = arg_parse()

    gt_folder = sorted(Path(args.gt_path).glob('./*'))
    pred_folder = sorted(Path(args.pred_path).glob('./*'))

    score_vls = []
    n_scores = 0
    for idx, gt in enumerate(gt_folder):
        pred = pred_folder[idx]

        # print(type(gt), gt)
        gt_img = CV2.imread(str(gt), 0)
        pred_img = CV2.imread(str(pred), 0)

        score = evaluate(gt_img, pred_img)
        score_vls.append(score)
        n_scores += 1

        print(f"{gt.name}: {score:.4f}")


if __name__ == '__main__':
    main()
