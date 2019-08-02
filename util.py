import requests
import json



APIKEY = ""

def get(url):
    resp = requests.get(url)
    if resp.ok:
        return resp.json()

def construct_city_id(cityname):
        with open("citylist.json", encoding="utf8") as citylist:
                citydata = json.load(citylist)
                for city in citydata:
                        if city["name"].lower() == cityname:
                                cityid = city["id"]
        return cityid

def getweather(cityname):
        
        cityname = cityname.lower()
        cityid = construct_city_id(cityname)

        # url = f"https://api.openweathermap.org/data/2.5/weather?APPID={APIKEY}&q={cityname}&units=metric"
        url = f"https://api.openweathermap.org/data/2.5/weather?APPID={APIKEY}&id={cityid}&units=metric"
        data = get(url)
        
        # if intent_name == "GetLocationWeather":
        #parse the cityid weather from the response
        weather = data['weather'][0]['description']
        return "{}".format(weather)

def getwindspeed(cityname):
        cityname = cityname.lower()
        cityid= construct_city_id(cityname)

        # url = f"https://api.openweathermap.org/data/2.5/weather?APPID={APIKEY}&q={cityname}&units=metric"
        url = f"https://api.openweathermap.org/data/2.5/weather?APPID={APIKEY}&id={cityid}&units=metric"
        data = get(url)
        
        # if intent_name == "GetLocationWeather":
        #parse the cityid weather from the response
        windspeed = data['wind']['speed']
        return windspeed

def gettemp(cityname):
        cityname = cityname.lower()
        cityid= construct_city_id(cityname)

        # url = f"https://api.openweathermap.org/data/2.5/weather?APPID={APIKEY}&q={cityname}&units=metric"
        url = f"https://api.openweathermap.org/data/2.5/weather?APPID={APIKEY}&id={cityid}&units=metric"
        data = get(url)
        
        # if intent_name == "GetLocationWeather":
        #parse the cityid weather from the response
        temperature = data['main']['temp']
        return temperature
