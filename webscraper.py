#Intro
#face_reader.py
#11/20/2017
#Danial Sahuri
#Description: Takes a website url saved in 'currentURL.txt' and parses the html for images
#downloads those images and renames them in numerical order from 1 onwards.

import os
import urllib
import numpy as np
import cv2
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pprint import pprint

#defines the function
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

# read the url from the created file
with open ("currentURL.txt", "r") as myfile:
    ourURL = myfile.read()
    print(ourURL)

#Counter starting at 1 to rename images
i=1
soup = make_soup(ourURL)
for img in soup.findAll('img'):
    temp=img.get('src')
    if temp[:1]=="/":
        image = ourURL + temp
    else:
        image = temp

    nametemp = img.get('alt')
    if len(nametemp)==0:
        filename=str(i)
        i=i+1
    else:
        continue

#Saves images
    imagefile = open("images/" + filename + ".jpg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
