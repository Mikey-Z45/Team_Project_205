import numpy as np
import numpy
import cv2
from pprint import pprint
from os import listdir
from os.path import isfile, join

mypath='images/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
  #for n in images:
