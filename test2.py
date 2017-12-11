import os
import numpy as np
import cv2
from pprint import pprint


for file in os.listdir("images/"):
    if file.endswith(".jpg"):
        print("success")
