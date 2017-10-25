import RPi.GPIO as GPIO
import time
import urllib2
from bs4 import BeautifulSoup
import json
import multiprocessing

def rain_prediction():

    appid= "4699d113f68be6cb422c9bb2c2997623"
    lat = "12.9807"  # LATITUDE
    lon = "74.8031"  # LONGITUDE

    rain_threshold = 10  # PARAMETER

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

    f = open("Prediction.txt", "w")
    f.write(str(rains))
    f.close()

def rain():
    f = open("Prediction.txt", "r")
    for lines in f:
        a = int(lines)
    f.close()
    return a

def setup():

    GPIO.setmode(GPIO.BOARD)

    out_pin = 12
    in_pin = 11
    switch = 15

    GPIO.setup(out_pin, GPIO.OUT)
    GPIO.setup(in_pin, GPIO.IN)
    GPIO.setup(switch, GPIO.IN)

def irrigate():

    try:
        while True:
            if GPIO.input(switch):
                GPIO.output(out_pin, GPIO.HIGH)
            else:
                if GPIO.input(in_pin) and rain()!=1:
                    GPIO.output(out_pin, GPIO.HIGH)
                else:
                    GPIO.output(out_pin, GPIO.LOW)
                    time.sleep(1)

    except KeyboardInterrupt:
        GPIO.output(out_pin, GPIO.LOW)
        GPIO.cleanup()

if __name__ == '__main__':

    poll_mins = 30  # PARAMETER
    minetime = poll_mins*60
    
    GPIO.setmode(GPIO.BOARD)

    out_pin = 12
    in_pin = 11
    switch = 15

    GPIO.setup(out_pin, GPIO.OUT)
    GPIO.setup(in_pin, GPIO.IN)
    GPIO.setup(switch, GPIO.IN)

    while True:
        rain_prediction()
        print(rain())
        p = multiprocessing.Process(target = irrigate)
        p.start()
        time.sleep(minetime)
        p.terminate()
        GPIO.output(out_pin, GPIO.LOW)
        p.join()
