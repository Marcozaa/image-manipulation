from cmath import pi
from turtle import width
import PIL.Image
import numpy as np
from PIL import Image

def getCorrectedImage(img):
    
    data = list(img.getdata())

    new_data = [(0, 0, 0)  if x[0]== x[1] and x[1] == x[2] and x[0] == 248 else (x[0]-200, x[1]-100, x[2]-100) for x in data]


    # we assign the tuple (0,0,0) if the pixel has the same R,G,B.
    # IN this way we can chage the image background color

    #else we substract from the figure R G Bs specific values.
    img.putdata(new_data)
    return img


def grayscale(img):
    data = list(img.getdata())

    new_data = [
    (int((x[0]+x[1]+x[2])/3), int((x[0]+x[1]+x[2])/3), int((x[0]+x[1]+x[2])/3)) for x in data]


    # we assign the tuple (0,0,0) if the pixel has the same R,G,B.
    # In this way we can chage the image background color
    #else we substract from the figure R G Bs specific values.
    img.putdata(new_data)
    return img

def main():
    image = PIL.Image.open("./catlow.jpg")
    size = width, height = image.size

    
    
    pixels = list(grayscale(image).getdata())

   # print(list(pixels))
    # Add new pixels to construct a new image
    dst_image = Image.new('RGB', (width, height))
    dst_image.putdata(pixels)  # Place pixels in the new image.
    dst_image.save('result.png')  # Save the new image.
    


main()

