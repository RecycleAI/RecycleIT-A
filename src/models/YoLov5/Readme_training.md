# Training with yolov5:



### Import useful libraries

> import os

> from random import choice

> import shutil

> import glob as glob

> from IPython.display import Image

> import torch

> !pip install -U albumentations==1.0.3

Note : Activate Albumentations to add more augmentation

> import yaml


> !pip install tensorboard==2.4.1

> %load_ext tensorboard

> %tensorboard --logdir runs file

*** 
### Command line for train model 
> ####  !python train.py --img <image_size> --batch <number_of_batch> --epochs <number_of_epoch> --data <yaml_file> --weights yolov5s.pt --project ,<result_directory> --name <filename> --cache --save-period <save_per_epoch>

