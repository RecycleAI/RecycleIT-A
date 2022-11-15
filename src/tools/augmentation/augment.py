
"""Augment.ipynb

# # Command for running cli in google colab
# %%writefile parsing.py
# 
# # Import Useful libraries 
# import torch 
# import argparse
# import torchvision
# 
# transform_list = []
# 
# # Define augment function
# def augment(img):
#   """
#   Enter a img_dir, batch, augment_dir and augmentations, 
#   : param img_dir : First input to augment
#   : type img_dir : str 
#   : param batch : Second input to augment
#   : type batch : unsigned int
#   : param augment_dir : Third input to augment
#   : type augment_dir : str
#   : param augment : Forth input to augment
#   : type augment : str
#   : param augment : Fifth input to augment
#   : type augment : str
#   : param augment : Sixth input to augment
#   : type augment : str  
#   """
# 
# # List of augmentations
#   transform_list.append(torchvision.transforms.Resize((640,640)))
#   
#   if img.random_horizontal_flip:
#     transform_list.append(torchvision.transforms.RandomHorizontalFlip(p=img.random_horizontal_flip/100))
# 
#   if img.random_vertical_flip:
#     transform_list.append(torchvision.transforms.RandomVerticalFlip(p=img.random_vertical_flip/100))
# 
#   if img.random_rotation:
#     transform_list.append(torchvision.transforms.RandomRotation(img.random_rotation))    
# 
#   transform_list.append(torchvision.transforms.ToTensor())   
#   transforms = torchvision.transforms.Compose(transform_list)  
# 
#   dataset = torchvision.datasets.ImageFolder(img.directory, transform=transforms)
#   dataloader = torch.utils.data.DataLoader(dataset, batch_size=img.batch, shuffle=False)
# 
#   num = len(transform_list)
#   img_type = img.directory.split("/")[-1].lower()
# 
#   for i in range(num):
#     images, labels = next(iter(dataloader))
#     
#     for j in range(img.batch):
#       image = images[j]
#       torchvision.utils.save_image(image, f'{img.augment_dir}/{img_type}{j+img.batch*i}.jpg')  
# 
# 
# # Prepare cli command
# if __name__=="__main__":
#   parser = argparse.ArgumentParser(
#         description="welocome to the bounding box finder"
#         )
# 
#   parser.add_argument(
#       "-dir","--directory", 
#       type=str,
#       help="Enter the directory of a image"
#     )
# 
#   parser.add_argument(
#       "--batch", 
#       type=int,
#       help="How many samples per batch to load"
#     )
# 
#   parser.add_argument(
#       "--augment_dir",
#        type=str,  
#        help="Directory of augmented image"
#        )
# 
#   parser.add_argument(
#       "--random_horizontal_flip", 
#       type = int,
#       choices = range(0,101,10),
#       help="Random Horizontal Flip"
#     )
#   parser.add_argument(
#       "--random_vertical_flip", 
#       type = int,
#       choices = range(0,101,10),
#       help="Random  Vertical Flip"
#     ) 
# 
#   parser.add_argument(
#       "--random_rotation", 
#       type = int,
#       choices = range(0,361),
#       help="Random Rotation"
#     )       
# 
# 
# 
#   parsed_args = parser.parse_args()
# 
# 
# augment(parsed_args)

# command line interface
!python3 parsing.py --directory <img_dir> --batch <num_batch> --augment_dir <save_dir> --random_horizontal_flip <pass_probablity> --random_rotation <degree_of_rotation>
# show a full description and help with using cli
!python3 parsing.py -h

