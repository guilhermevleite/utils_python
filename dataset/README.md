# Scripts Regarding Dataset Manipulation|Organization

## [augmentation](augmentation.py)

Augment dataset images with Albumentations, and save to disk.

## [delete_unpaired](delete_unpaired.py)

Some datasets are not paired between inputs and masks, this script deletes any data that has no pair.

## [rename_bulk](rename_bulk.py)

Rename files in bulk to remove a pattern. My pipelines assume that every input has a corresponding mask with the same name. This script is useful to rename inputs and masks into the same pattern.

## [sartorious](sartorious.py)

Sartorius is a dataset.
TODO: Document this file.

## [split_paired](split_paired.py)

Split the dataset into Train and Validation data.
