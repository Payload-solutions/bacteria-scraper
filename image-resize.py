

from PIL import Image
import os
from pprint import pprint


BASE_DIR = "lactobacillus/"
NEW_DIR = "images/"


def main():
    # base = os.path.join(BASE_DIR)
    base = [data for data in os.listdir(NEW_DIR)]
    for pos, x in enumerate(base):
        read_image = Image.open(os.path.join(NEW_DIR, x))
        # print(read_image)
        name = f"{NEW_DIR}lactobacillus_{pos+len(base)}.png"
        
        img_format = read_image.format
        new_image = read_image.rotate(180)
        new_image.save(name)

    # pprint(base)

if __name__ == "__main__":
    main()
