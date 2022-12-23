# Augmentation
***

- ### Import useful libraries

> import torch

> import torchvision
 
> import argparse

- ### Define an augment function to apply augmentation to the dataset

*** 
***Cli Augment function***
> !python3 parsing.py --directory <img_dir> --batch <num_batch> --augment_dir <save_dir> --random_horizontal_flip <pass_probablity>  --random_vertical_flip<pass_probablity>  --random_rotation <degree_of_rotation> 


The inputs of this function are as below:

- --directory: the directory of the image folder 
- --batch: the number of data passed to the program 

- --augment_dir: folder to store augmented data

Defined Augmentations
- --random_horizontal_flip
- --random_vertical_flip
- --random_rotation