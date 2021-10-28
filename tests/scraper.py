#!/usr/bin/python

from urllib.parse import urlencode
import re
from bs4 import BeautifulSoup
import requests
from pprint import pprint

class Scraper:
    """To make possible implement convolutional neuron networks, it's necessary 
    extract the specific images, i.e. bacteria growth.
    """
    def __init__(self, url: str) -> None:
        self.url = url
    
    def __repr__(self):
        pass
    
    def __len__(self):
        pass
    
    def extract_images(self):
        pass


def scrap_images() -> None:
    
    base_url = "https://www.scienceprofonline.com/science-image-libr/"\
    "sci-image-libr-bacteria-media-culture-lab.html"

    page = requests.get(url=base_url).text
    html = BeautifulSoup(page, 'lxml')
    response = [image["src"] for image in html.findAll('img')]
    
    for src in response:
        match = re.search(r'.*.jpg$', src)
        if match:
            print(match.group())
        else:
            continue
         
    

def main():
    scrap_images()


if __name__ == "__main__":
    main()
