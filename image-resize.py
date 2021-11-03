

from PIL import Image
import os
from pprint import pprint


BASE_DIR = "streptococcus/"
NEW_DIR = "images/"


def main():
    # base = os.path.join(BASE_DIR)
    base = [data for data in os.listdir(BASE_DIR)]
    for pos, x in enumerate(base):
        read_image = Image.open(os.path.join(BASE_DIR, x))
        # print(read_image)
        name = f"{NEW_DIR}streptococcus_{pos+2+len(base)}.png"
        
        # img_format = read_image.format
        # new_image = read_image.resize((64,64))
        # new_image = read_image.convert('L')
        new_image = read_image.rotate(90)
        new_image.save(name)

    # pprint(base)

if __name__ == "__main__":
    main()
