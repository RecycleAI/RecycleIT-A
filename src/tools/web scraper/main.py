# Importing libraries

import os

import numpy as np
from google_images_download import google_images_download
import argparse


response = google_images_download.googleimagesdownload() 


# Rename the downloaded images
def renaming(query):
    """
    keyword: item you want to search in google
    """
    path = os.path.join("images", query)
    dir_list = os.listdir(path)
    print(dir_list)
    for i, img in enumerate(dir_list):

        old_name = os.path.join(path, img)
        new_name = os.path.join(path, str(i) + ".jpg")
        os.rename(old_name, new_name)

# google image downloader
def downloadimages(query, limit):

    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit":limit,
                 "print_urls":False,
                 "output_directory": "images",
                 "aspect_ratio":"panoramic"
                 }
    try:
      response.download(arguments)
    except FileNotFoundError:
      pass
    renaming(query)

# Loop over the list of queries
def image_scraper(queries, limit):
  for query in queries:
      downloadimages(query, limit) 
      print() 

def main():
    limit = 20
    queries = [      
    'hdpe plastic trash','pet plastic trash'
    ]

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-SQ", "--SearchQueries", help="Queries you want search with comma between and in a quotation mark")
    parser.add_argument("-l", "--Limit", help="Number of images per search query you want to collect")

    # Read arguments from command line
    args = parser.parse_args()

    if args.SearchQueries:
        queries = [args.SearchQueries]
    if args.Limit:
        limit = args.Limit
    image_scraper(queries, limit)


if __name__ == "__main__":
    main()
