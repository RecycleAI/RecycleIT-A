# How to receive a bounding box for an image dataset

***
## 1. detect.py
### First we go through the instalation process :

1. Install torch
> #### !pip install torch

 2. Import torch and Image (for visualization)
> #### import torch 

> #### from IPython.display import Image

3. Clone yolov5 github
> #### !git clone https://github.com/ultralytics/yolov5

4. Install requirements.txt for yolov5
> #### !pip install -r /content/yolov5/requirements.txt



### Next, by running the following code we receive a bounding box and label for every passed image :

> #### !python detect.py --source <...> --weights <...> --imgsz <...> --save-conf --save-txt --project <...> --name <...> 

#### Description of the above code :
- --source : after this, we should pass the images file

- --weights : after this command, the weight of the trained model is passed

- --imgsz : to determine inference size h,w 

- --save-txt : As we want a yolo format bounding box for each image and level of confidence --save-txt should be written to save results

- --save-conf : to save confidences this is passed 

  > #### Note: --save-conf saves confidences in --save-txt labels

- --project : to save results to project/name

- --name : name of the folder showing the result



### In the final step, to illustrate the image run the following code:

> #### Image(filename= "path of predicted image")


***
## 2. Creating an automatic labeling tools with torch.hub

This code was run in google colab


#### Clone yolov5 repository

>  !git clone https://github.com/ultralytics/yolov5


#### Install yolov5 requirements
>  !pip install -r /content/yolov5/requirements.txt


##### Note: The two above commands must run separately from the rest of the code to prepare the yolov5 model
***
#### Command for running cli in google colab
>  %%writefile parsing.py

#### Import Useful libraries 
>  import torch
 
>  import argparse

#### CLI 
>  !python3 parsing.py -c <level_of_confidence> --path <image_directory> -w <weight_of_trained_model>

##### Note: In the second code, we add one more options to show detected object with the highest confidence percentage
***
***
## How to run python files without typing python
Steps to follow to run your python code without typing **python filename.py**.

You can simply run by typing filename if you follow these simple steps.

**Step 1 : Add shebang line as first line in your python code**
> !/usr/bin/python3

This line tells about the location of interpreter.

**Step 2 : Make your python file executable**

In terminal, go to your directory where your python file is located and type the below command.

> chmod +x filename.py

For example we have hello.py as our file, so we will move to the directory where it is located and will do

> chmod +x hello.py

Now you can run your python file like ./hello.py
