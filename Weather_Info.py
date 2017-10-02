"""
Obtains Weather Data from the internet and logs it.

"""

import pyowm

owm = pyowm.OWM('4699d113f68be6cb422c9bb2c2997623')

observation = owm.weather_at_place('London,uk')
# observation = owm.weather_at_place('Mangalore, IN')
w = observation.get_weather()
print("Wind")
print(w.get_wind())
print("Humidity")
print(w.get_humidity())
print("Temperature in Celcius")
print(w.get_temperature('celsius'))
