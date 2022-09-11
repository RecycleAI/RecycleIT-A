# Importing libraries

import os

import numpy as np
from google_images_download import google_images_download


response = google_images_download.googleimagesdownload() 

# list of queries you want to search
search_queries = [      
'hdpe plastic trash',
'pet plastic trash'
]

# Rename the downloaded images
def renaming(keyword):
    """
    keyword: item you want to search in google
    """
    path = os.path.join("images", keyword)
    dir_list = os.listdir(path)
    print(dir_list)
    for i, img in enumerate(dir_list):

        old_name = os.path.join(path, img)
        new_name = os.path.join(path, str(i) + ".jpg")
        os.rename(old_name, new_name)

# google image downloader
def downloadimages(keyword):

    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit":20,
                 "print_urls":False,
                 "output_directory": "images",
                 "aspect_ratio":"panoramic"
                 }
    try:
      response.download(arguments)
    except FileNotFoundError:
      pass
    renaming(keyword)

# Loop over the list of queries
for query in search_queries:
    downloadimages(query) 
    print() 
