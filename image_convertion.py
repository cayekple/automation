#!/usr/bin/env python3

from PIL import Image
import os, sys

def process_image(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            image, ext = os.path.splitext(file)
            convert_image(image)
        break

def resize_image():
    pass

def rotate_image():
    pass

def convert_image(image, ext='jpeg'):
    size = (128, 128)
    try:
        with Image.open('./images/'+image) as im:
            im.thumbnail(size)
            im.rotate(-90)
            im.convert('RGB').save('/opt/icons/'+image, ext)
    except OSError:
        print('cannot create thumbnail', image)
    return


process_image('./images')

