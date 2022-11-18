FOLDER=~/workspace/deep_learning/datasets/segmentation/ours_2021_96/masks/0

for file in "$FOLDER"/*; do
    echo $file
    python normalize.py --input $file
done
