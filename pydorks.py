#!/usr/bin/python


class GoogleDork:

    def __init__(self):
        self.google_url = "www.google.com/search/"
        self.in_title = "intitle:"
        self.allin_text = "allintext:"
        self.in_url = "inurl:"
        self.site = "site:"
        self.file_type = "filetype:"
        self.link = "link:"
        self.cache = "cache:"
        self.info = "info:"

    def __repr__(self):
        return f"URL base for the dorking are {self.google_url}"


    def query_parameters(self) -> str:
        """Basically, we gonna struct the url for the dorking.
        The goal is start with the right paramters"""
        
        ress = requests.get(url=self.google_url+""+"/")

def main():
    google = GoogleDork()
    print(google)


if __name__ == "__main__":
    main()
