import os
import urllib
import numpy as np
import cv2
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pprint import pprint


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

# read the url from the created file
with open ("currentURL.txt", "r") as myfile:
    ourURL = myfile.read()
    # print(ourURL)

    
i=1
soup = make_soup(ourURL)
for img in soup.findAll('img'):
    temp = img.get('src')
    if temp[:1] == "/":
        image = ourURL + temp
    else:
        image = temp

    nametemp = img.get('alt')
    if len(nametemp)==0:
        filename=str(i)
        i=i+1
    else:
        filename=nametemp


    imagefile = open("images/" + filename + ".jpg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()

img = cv2.imread('1.jpg')

print(type(img))

print(img.shape)

print(img.dtype)

gray_img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

print(gray_img.shape)

key = cv2.waitKey()
pic_remap = cv2.applyColorMap(gray_img, cv2.COLORMAP_WINTER)
pic_remap1 = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)
pic_remap2 = cv2.applyColorMap(gray_img, cv2.COLORMAP_BONE)
while True:
    cv2.imshow("Final Project 205", img)
    key = cv2.waitKey()
    if ord('q') == key:
        break
    elif ord('g') == key:
        img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
    elif ord('h') == key:
        img = pic_remap
    elif ord('j') == key:
        img = pic_remap1
    elif ord('b') == key:
        img = pic_remap2
    elif ord('c') == key:
        img = cv2.imread('1.jpg')
