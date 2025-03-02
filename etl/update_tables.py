
import csv
from data.weather_list import weather_list
from config.sqlalchemy_config import engine,text

def load_new_cities(countriesDict):
    """
    DEPRECATED \n
    Update 'd_cities' table in the connected DB
    then update 'city_id's file
    :param countriesDict:
    :return:
    """
    #Insert new unique cities into d_cities
    with engine.connect() as conn:
        if True:
            for country,city_dict in countriesDict.items():
                for city,cords_list in city_dict.items():
                    lat=cords_list[0]
                    lon=cords_list[1]
                    conn.execute(text(f"""
                        INSERT INTO d_cities (city_name,country_name,lat,lon)
                        SELECT 
                            '{city}' as city_name,
                            '{country}' as country_name,
                            {lat} as lat,
                            {lon} as lon
                        ON CONFLICT DO NOTHING
                                """))
                    conn.commit()

def update_local_city_data():
    """
    Gets (id,city_name,country_name,lat,lon) and saves it locally in 'city_id'
    :return:
    """
    with engine.connect() as conn:
        #Update 'city_id's in countries file
        with open(f"../data/city_id.csv", 'w') as city_id_csv_file:
            res = conn.execute(text(
f"""
SELECT id,city_name,country_name,lat,lon
from d_cities
"""))
            for entry in res:
                csv.writer(city_id_csv_file,lineterminator='\n').writerow(entry)

def load_new_weather(weather_list):
    with engine.connect() as conn:
        for item in weather_list:
            conn.execute(text(f"""
            INSERT INTO d_weather (id,condition,description)
            SELECT {item[0]} as id,'{item[1]}' as condition,'{item[2]}' as description
            """))
            conn.commit()

update_local_city_data()
#load_new_weather(weather_list)
#load_new_cities(countries_dict)
