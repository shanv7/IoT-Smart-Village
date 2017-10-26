import urllib2
from bs4 import BeautifulSoup
import json
import multiprocessing
import time

def rain_prediction():

    appid= "4699d113f68be6cb422c9bb2c2997623"
    lat = "12.9807"
    lon = "74.8031"

    rain_threshold = 10

    url = "http://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+lon+"&appid="+appid
    # print(url)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    json_data = soup.get_text()
    s = json.loads(json_data)
    # print(s)

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
    
    f = open("Prediction.txt", "r")
    for lines in f:
        a = int(lines)
    print(a)
    f.close()

if __name__ == '__main__':
    #p = multiprocessing.Process(target = rain_prediction)
    #p.start()
    #time.sleep(5)
    #p.terminate()
    #p.join()
    rain_prediction()
    



# id_list = list()
# rain_list = list()

# for i in range(0, 40):
#     id_list.append(s["list"][i]["weather"][0]["id"])
#     try:
#         rain_list.append(s["list"][i]["rain"]["3h"])
#     except:
#         rain_list.append(0)
#         continue
# print(id_list)
# print(rain_list)
