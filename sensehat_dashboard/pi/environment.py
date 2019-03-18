
import requests
import threading
import time
from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore
from sense_hat import SenseHat

app = Flask(__name__)
sense = SenseHat()

cred = credentials.ApplicationDefault()
environment_app = firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://pi-server-cc2b0.firebaseio.com/',
  'databaseAuthVariableOverride': {
    'uid': 'environment_updater'
  }
})

# Create instance of firestore
db = firestore.client()
