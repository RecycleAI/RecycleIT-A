# Detection
### Useful libraries
> !pip install torch 


> from IPython.display import Image


### Clone repository
> !git clone https://github.com/ultralytics/yolov5

### Install requirements of yolov5
> !pip install -r /content/yolov5/requirements.txt



*** 

!python detect.py --source <file_path> --weights <weight_of_trained_model> --imgsz <size_of_img> --save-conf --save-txt --project <result_dir> --name <filename>

***
# Convert weights to onnx
- ### Clone repository 
> !git clone https://github.com/ultralytics/yolov5  

- ### Install Onnx
> !pip install onnx==1.9.0

> !pip install -r requirements.txt 

- ### Convert weights from pt format to Onnx format

#### !python export.py --weights <weight_of_trained_model> --img <img_size> --include onnx