# How to Run code

## 1. Create a new environment
```
$ conda create --name image_scraper python=3.8
```
## 2. Clone repository
Clone this repository

```
$ git clone https://github.com/RecycleAI/RecycleIT-A.git
```
## 3. Change your directory
```
$ cd ./RecycleIT-A/src/tools/'web scraper'
```
## 4. Install requirements
```
$ pip install -r requirements.txt
```
## 5. argument parsers

* -l --limit: Number of images per search query you want to collect
* -SQ --SearchQueries: Queries you want search with comma between and in a quotation mark
* -h --help: To display arguments explanations

## 6. Run the code

```
$ pyhton3 main.py -l 5 -SQ 'hdpe plastic trash','pet plastic trash'
```
