from PIL import Image
import os

def create_ico():
    img = Image.open('assets/icon.png')
    img.save('assets/icon.ico', format='ICO')

if __name__ == "__main__":
    create_ico() 