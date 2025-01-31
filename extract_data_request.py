
from sqlalchemy_config import engine,text
import requests as req
import csv
import os

def etl_current():
    with open(fr"city_id.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        with engine.connect() as conn:
            for row in csv_reader:
                res = req.get(f"https://api.openweathermap.org/data/2.5/weather?lat={row[3]}&lon={row[4]}&appid={os.getenv('OPEN_WEATHER_KEY')}").json()
                #Check if all the data is present
                try:
                    wind_speed=f"{res['wind']['speed']} as wind_speed,"
                except:
                    wind_speed=f"NULL as wind_speed,"
                try:
                    wind_deg=f"{res['wind']['deg']} as wind_deg,"
                except:
                    wind_deg=f"NULL as wind_deg,"
                try:
                    wind_gust=f"{res['wind']['gust']} as wind_gust,"
                except:
                    wind_gust=f"NULL as wind_gust,"
                try:
                    rain=f"{res['rain']['1h']} as rain,"
                except:
                    rain=f"NULL as rain,"
                try:
                    clouds=f"{res['clouds']['all']} as clouds,"
                except:
                    clouds=f"NULL as clouds,"
                #

                if len(res["weather"]) == 1:
                    conn.execute(text(f"""
                        INSERT INTO f_all_data (city_id,weather_id,temp,feels_like,temp_min,temp_max,pressure,humidity,sea_level,grnd_level,wind_speed,wind_deg,wind_gust,rain,clouds,time_zone)
                        SELECT 
                            {row[0]} as city_id,
                            {res["weather"][0]["id"]} as weather_id,
                            {res["main"]["temp"]} as temp,
                            {res["main"]["feels_like"]} as feels_like,
                            {res["main"]["temp_min"]} as temp_min,
                            {res["main"]["temp_max"]} as temp_max,
                            {res["main"]["pressure"]} as pressure,
                            {res["main"]["humidity"]} as humidity,
                            {res["main"]["sea_level"]} as sea_level,
                            {res["main"]["grnd_level"]} as grnd_level,
                            {wind_speed}
                            {wind_deg}
                            {wind_gust}
                            {rain}
                            {clouds}
                            {res["timezone"]} as time_zone
                    """))
                    conn.commit()


etl_current()