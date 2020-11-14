import requests
import pprint
import sys
import pandas as pd

# Script to find co-ordinates of the coloseum in Rome
API_KEY = sys.argv[0]

API_ENDPOINT = "http://maps.googleapis.com/maps/api/geocode"
KEY = API_KEY # Enter API KEY here
ADDR_LIST = pd.read_csv("rome_landmarks.csv", sep="|")
coordinates = []

for ADDR in ADDR_LIST:
    ADDR = ADDR.replace(" ", "+")
    RES = requests.get(f"{API_ENDPOINT}/json?address={ADDR}&key={KEY}").json()
    LAT = RES["results"][0]["geometry"]["location"]["lat"]
    LONG = RES["results"][0]["geometry"]["location"]["lng"]
    coordinates.append((LAT, LONG))
# Done

