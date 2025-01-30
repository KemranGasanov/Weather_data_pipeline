
import os
from countries import countries_dict
from sqlalchemy_config import engine,text

def load_new_cities(countriesDict):
    with engine.connect() as conn:
        for country,city_dict in countriesDict.items():
            for city,cords_list in city_dict.items():
                lat=cords_list[0]
                lon=cords_list[1]
                conn.execute(text(f"INSERT INTO d_cities (city_name,country_name,lat,lon)"
                             f"SELECT '{city}' as city_name,"
                             f"'{country}' as country_name,"
                             f"{lat} as lat,"
                             f"{lon} as lon"))
                conn.commit()



def load_new_weather():
    pass

load_new_cities(countries_dict)
