#!/usr/bin/python

from typing import List
import requests

"""
Url encoding, it's neccessary using urllib to encoding
Returns:
    [type]: [description]
"""

class GoogleDork:

    def __init__(self):
        self.google_url = "www.google.com/search"
        self.in_title = "intitle:"
        self.allin_text = "allintext:"
        self.in_url = "inurl:"
        self.site = "site:"
        self.file_type = "filetype:"
        self.link = "link:"
        self.cache = "cache:"
        self.info = "info:"
        self.or_operator = "|"
        self.and_operator = "+"
        self.tags:List[str] = list()

    def __repr__(self):
        return f"URL base for the dorking are {self.google_url}"
    



    def query_parameters(self) -> str:
        """Basically, we gonna struct the url for the dorking.
        The goal is start with the right paramters"""
        
        # base_url = self.google_url+"?q=intitle:\"Lactobacillus Bulgaricus\""
        
        # base_url = "https://www.google.com/search?q=intitle%3A%22Lactobaciullus+Bulgaricus%22"
        base_url = """https://www.google.com/search?q=intitle:%22Lactobacillus%20bulgaricus%22"""
        response = requests.get(url=base_url).text
        with open("index.html", "w") as file:
            file.write(response)
        

def main():
    google = GoogleDork()
    google.query_parameters()


if __name__ == "__main__":
    main()
