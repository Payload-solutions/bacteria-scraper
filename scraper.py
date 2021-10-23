#!/usr/bin/python

import re
# from bs4 import BeautifulSoup
import requests
from pprint import pprint

class Scraper:
    def __init__(self):
        pass


def scrap_images() -> None:
    
    """with open("url-sites.txt", "r") as url:
        urls = [url_.strip("\n") for url_ in url.readlines()]
    """

    with open("index.html", "r") as f:
        file = f.read()
    """for site in urls:
        # page = requests.get(url=site).text
        # html = BeautifulSoup(page, 'html.parser')
        # pprint(html.find_all('img', {'src'}))
        # print(html)
        # match = re.findall(r'\<img src=.*', page)
        # pprint(match.group())
    """
    # print(file)
    # match = re.findall(r'src="(.*[.jpg]$)"', file)
    match = re.findall(r'src="(.*\.jpg\)"', file)
    pprint(match)

def main():
    scrap_images()


if __name__ == "__main__":
    main()
