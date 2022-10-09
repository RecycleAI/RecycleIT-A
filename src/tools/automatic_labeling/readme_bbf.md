# How to receive a bounding box for an image dataset

***
### First
 - 1. Install torch
> !pip install torch

 - 2. Import torch and Image (for visualization)
>import torch 

>from IPython.display import Image

 - 3. Clone yolov5 github
> !git clone https://github.com/ultralytics/yolov5

4. Install requirements.txt for yolov5
> !pip install -r /content/yolov5/requirements.txt

### Then run detect.py for prediction
***
## Detection
> !python detect.py --source <...> --weights <...> --imgsz <...> --save-conf --save-txt --project <...> --name <...> 

Description of the above code
- --source : after this, we should pass the images file

- --weights : after this command, the weight of the trained model is passed

- --imgsz : to determine inference size h,w 

- --save-txt : As we want a yolo format bounding box for each image and level of confidence --save-txt should be written to save results

- --save-conf : to save confidences this is passed 
### Note: --save-conf saves confidences in --save-txt labels

- --project : to save results to project/name

- --name : name of the folder showing the result

To illustrate images :
> Image(filename=....)

