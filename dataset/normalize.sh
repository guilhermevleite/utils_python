FOLDER=~/workspace/deep_learning/datasets/segmentation/ours_2021_48/masks/0

for file in "$FOLDER"/*; do
    echo $file
    python normalize.py --input $file
done

# FOLDER=~/Downloads/72
#
# for file in "$FOLDER"/*; do
#     echo $file
#     python normalize.py --input $file
# done
#
# FOLDER=~/Downloads/96
#
# for file in "$FOLDER"/*; do
#     echo $file
#     python normalize.py --input $file
# done
