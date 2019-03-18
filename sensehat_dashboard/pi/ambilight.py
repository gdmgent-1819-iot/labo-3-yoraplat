
import requests
import threading
import time
from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore
from sense_hat import SenseHat

# Create instance of Flask
app = Flask(__name__)

# Create instance of sensehat
sense = SenseHat()


# Function to set pixels
def setPixels(state, color):
  if(state == 'on'):
    color = color.lstrip('#')
    color_pixel = tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))
    for x in range(0,8):
      for y in range(0,8):
        sense.set_pixel(x, y, color_pixel)
  else:
    sense.clear()
