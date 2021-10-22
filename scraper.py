#!/usr/bin/python

import re
from bs4 import BeautifulSoup
import requests
from pprint import pprint

class Scraper:
    def __init__(self):
        pass


def scrap_images() -> None:
    
    with open("url-sites.txt", "r") as url:
        urls = [url_.strip("\n") for url_ in url.readlines()]
    
    for site in urls:
        page = requests.get(url=site).text
        # html = BeautifulSoup(page, 'html.parser')

        match = re.search(r'\<img src=(.*)>', page)
        pprint(match.group())
    

def main():
    scrap_images()


if __name__ == "__main__":
    main()
