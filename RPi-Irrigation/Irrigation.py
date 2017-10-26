"""
Irrigation System:

Data:
1. Soil Moisture Sensor Data
2. Rain Prediction for the next 3 hours
3. Manual Switch

Notes:
1. Manual Switch overrides any sensor or web data.
2. If soil wetness is below a threshold, outlet is automatically opened.
3. If rain is predicted in the next 3 hours, outlet is closed unless
    manually opened.
4. In case of error / sensor malfunctions, remove Vcc (Red Jumper).

Demonstration:
1. Uncomment 3 lines and comment the 3 previous lines. This will generate a
    random number every 3 seconds to emulate rain prediction data.

"""

import RPi.GPIO as GPIO
import time
import urllib2
from bs4 import BeautifulSoup
import json
import multiprocessing
from numpy.random import randint as random

def rain_prediction():

    appid= "OPENWEATHERMAP-API-KEY"
    lat = "12.9807"  # LATITUDE
    lon = "74.8031"  # LONGITUDE

    rain_threshold = 8  # PARAMETER: Rain in mm

    url = "http://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+lon+"&appid="+appid
    # print(url)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    json_data = soup.get_text()
    s = json.loads(json_data)

    # weather_id = s["list"][0]["weather"][0]["id"]
    try:
        rains = s["list"][0]["rain"]["3h"]
        if rains > rain_threshold:
            rains = 1
        else:
            rains = 0
    except:
        rains = 0

    return rains


def irrigate():
    poll_hours = 1 # PARAMETER: How often do we poll weather data?
    # poll_hours = 0.0009  # UNCOMMENT TO TEST
    poll_time = poll_hours*3600
    r = rain_prediction()
    # r = random(2)  # UNCOMMENT TO TEST
    print(r)
    prev = time.time()
    try:
        while True:
            
            if time.time()-prev > poll_time:
                r = rain_prediction()
                # r = random(2)  # UNCOMMENT TO TEST
                print(r)
                prev = time.time()
            
            if r == 1:
                GPIO.output(rain_led, GPIO.HIGH)
            else:
                GPIO.output(rain_led, GPIO.LOW)

            if GPIO.input(switch):
                GPIO.output(out_pin, GPIO.HIGH)
            else:
                if GPIO.input(in_pin) and r!=1:
                    GPIO.output(out_pin, GPIO.HIGH)
                else:
                    GPIO.output(out_pin, GPIO.LOW)
                    time.sleep(1)

    except KeyboardInterrupt:
        GPIO.output(out_pin, GPIO.LOW)
        GPIO.output(rain_led, GPIO.LOW)
        GPIO.cleanup()

if __name__ == '__main__':

    GPIO.setmode(GPIO.BOARD)

    out_pin = 12
    in_pin = 11
    switch = 15
    rain_led = 16

    GPIO.setup(out_pin, GPIO.OUT)
    GPIO.setup(rain_led, GPIO.OUT)
    GPIO.setup(in_pin, GPIO.IN)
    GPIO.setup(switch, GPIO.IN)

    irrigate()
    
