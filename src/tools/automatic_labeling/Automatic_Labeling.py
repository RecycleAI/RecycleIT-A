# Clone yolov5 repository
!git clone https://github.com/ultralytics/yolov5
    
# Install yolov5 requirements
!pip install -r /content/yolov5/requirements.txt

# Command for running cli in google colab
%%writefile parsing.py

# Import Useful libraries 
import torch 
import argparse


# Define function of model
def bounding_box_finder(img):
  """
  Enter a image path and a number and a weight using cli  
  : param path : First input to bounding_box_finder
  : type path : str 
  : param confidence : Second input to bounding_box_finder
  : type confidence : int 
  : param weight : Third input to bounding_box_finder
  : type weight : str
  """

  count = 0   # number of detected image

# Detect object using yolov5 
  model = torch.hub.load('ultralytics/yolov5', 'custom', path=img.weight)
  results = model(img.path)
  results.save()

    
# Remove no detection and show the detected object if its confidence higher than or equal to the passing number 

  for i in range(len(img.path)):
    if len(results.pandas().xyxy[i].index)==0:
      print(f"I am unable to draw bounding box for: {img.path[i]}")
      print("-----------------------")
      i+=1
    else:
      if results.pandas().xyxy[i].confidence[0]*100 >= img.confidence:
        count+=1  
        print(f"{results.pandas().xyxy[i]}")
        print(f"is result for {img.path[i]}")
        print(f"Model predict {count}  images from {len(img.path)}") 
        print("----------------------") 
        i+=1
        
          
      else:
        print(f"I am unable to draw bounding box for: {img.path[i]}  with choosen confidence")
        print("----------------------") 



# Prepare cli command

if __name__=="__main__":
  parser = argparse.ArgumentParser(
        description="welocome to the bounding box finder"
        )

  parser.add_argument(
      "-c","--confidence", 
      type=int,
      choices=range(0,100, 10),
      help="Enter a number between 0 to 1"
    )

  parser.add_argument(
      "--path",
       type=str, 
       nargs= "+", 
       help="Enter the directory of a image"
       )

  parser.add_argument(
      "-w","--weight", 
      type=str,
      help="Enter weights of yolov5 training"
    )     


  parsed_args = parser.parse_args()
bounding_box_finder(parsed_args)

# command line interface
!python3 parsing.py -c <level_of_confidence > --path <img_dir> -w <weight_dir>
# show a full description and help with using cli
!python3 parsing.py -h

###############################

# The following program only shows detected the object with the highest confidence percentage

# Clone yolov5 repository
!git clone https://github.com/ultralytics/yolov5
    
# Install yolov5 requirements
!pip install -r /content/yolov5/requirements.txt

# Command for running cli in google colab
%%writefile parsing.py

# Import Useful libraries 
import torch 
import argparse


# Define function of model
def bounding_box_finder(img):
  """
  Enter a image path and a number and a weight using cli  
  : param path : First input to bounding_box_finder
  : type path : str 
  : param confidence : Second input to bounding_box_finder
  : type confidence : int 
  : param weight : Third input to bounding_box_finder
  : type weight : str
  """

  count = 0    # number of detected image


# Detect object using yolov5 
  model = torch.hub.load('ultralytics/yolov5', 'custom', path=img.weight)
  results = model(img.path)
  results.save()


# Remove no detection and show the detected object if its confidence higher than or equal to the passing number
  for i in range(len(img.path)):
    if len(results.pandas().xyxy[i].index)==0:
      print(f"I am unable to draw bounding box for: {img.path[i]}")
      print("-----------------------")
      i+=1
    else:
      if results.pandas().xyxy[i].confidence.max()*100 >= img.confidence:
        count+=1  
        print(f"{results.pandas().xyxy[i].loc[results.pandas().xyxy[i].confidence.idxmax()]}")
        print(f"is result for {img.path[i]}")
        print(f"Model predict {count}  images from {len(img.path)}") 
        print("----------------------") 
        i+=1
        
          
      else:
        print(f"I am unable to draw bounding box for: {img.path[i]}  with choosen confidence")
        print("----------------------") 


# Prepare cli command
if __name__=="__main__":
  parser = argparse.ArgumentParser(
        description="welocome to the bounding box finder"
        )

  parser.add_argument(
      "-c","--confidence", 
      type=int,
      choices=range(0,100),
      help="Enter a number between 0 to 1"
    )

  parser.add_argument(
      "--path",
       type=str, 
       nargs= "+", 
       help="Enter the directory of a image"
       )

  parser.add_argument(
      "-w","--weight", 
      type=str,
      help="Enter weights of yolov5 training"
    )     



  parsed_args = parser.parse_args()


bounding_box_finder(parsed_args)

# Command line interface
!python3 parsing.py -c <level_of_confidence > --path <img_dir> -w <weight_dir>
# Show a full description and help with using cli
!python3 parsing.py -h
