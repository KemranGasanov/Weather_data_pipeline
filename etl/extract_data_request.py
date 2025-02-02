
from config.sqlalchemy_config import engine,text
import requests as req
import csv
import os

def etl(timeframe='current'):
    if timeframe=='current':
        url=f'https://api.openweathermap.org/data/2.5/weather'
    elif timeframe=='4d_forecast':
        url=f'' #TODO add new forecast functionality...
    else:
        raise Exception("Invalid timeframe, options: current, 4d_forecast")
    with open(fr"../city_id.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        #Try adding new data
        with engine.connect() as conn:
            try:
                for row in csv_reader:
                    res = req.get(f"{url}?lat={row[3]}&lon={row[4]}&appid={os.getenv('OPEN_WEATHER_KEY')}")
                    if 399 < res.status_code < 500:
                        raise Exception(fr"Client error has occurred when connecting to the API {res.status_code}")
                    res = res.json()
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
                    if len(res["weather"])>1:
                        weather_id="{"
                        for entry in res["weather"]:
                            weather_id+=f"{entry['id']},"
                        weather_id=(weather_id[::-1].replace(',','',1)[::-1])
                        weather_id+='}'
                    else: weather_id='{'+f"{res['weather'][0]['id']}"+'}'
                    conn.execute(text(f"""
                            INSERT INTO f_all_data (city_id,weather_id,temp,feels_like,temp_min,temp_max,pressure,humidity,sea_level,grnd_level,wind_speed,wind_deg,wind_gust,rain,clouds,time_zone,creation_date)
                            SELECT 
                                {row[0]} as city_id,
                                '{weather_id}'::INT[] as weather_id,
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
                                {res["timezone"]} as time_zone,
                                NOW() as creation_date
                        """))
                    conn.commit()
            except Exception as ex:
                print("Exception interrupted ETL procedure")
                print(fr"{ex}")
            finally:
                conn.close()