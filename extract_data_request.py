
from countries_list import countries_list
import requests

lat = 51.30
lon = 0.08
key = '5c58af63f604430c877305fd7ea0b31f'
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
res = requests.get(url)





