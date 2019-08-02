from flask import Flask, Response, request
import json

from util import *

app = Flask(__name__)

def getCityIntentHandler(cityname):
    # cityname = "".join( cityname.split() )
    weather = getweather(cityname)
    return f"The weather of {cityname} is {weather}"

def getTemperatureIntentHandler(cityname):
    # cityname = "".join( cityname.split() )
    temperature = gettemp(cityname)
    return f"The temperature of {cityname} is {temperature} degrees celsius."

def getWindIntentHandler(cityname):
    # cityname = "".join( cityname.split() )
    windspeed = getwindspeed(cityname)
    if windspeed < 1:
        windspeed = "Calm"
    elif 1 <= windspeed <= 5:
        windspeed = "Light"
    elif 5 < windspeed <= 11:
        windspeed = "Light breeze"
    else:
        windspeed = "Strong" 
    return f"The wind of {cityname} is {windspeed}"

@app.route("/", methods = ["POST"])
def main():
    
    req = request.get_json(silent=True, force=True)
    print(req)
    intent_name = req["queryResult"]["intent"]["displayName"]

    if intent_name == "GetLocationWeather":
        cityname = req["queryResult"]["parameters"]["cityname"]
        # humidity = req["queryResult"]["parameters"]["humidity"]
        resp_text = getCityIntentHandler(cityname)
    elif intent_name == "GetLocationTemperature":
        cityname = req["queryResult"]["parameters"]["cityname"]
        resp_text = getTemperatureIntentHandler(cityname)
    elif intent_name == "GetLocationWindSpeed":
        cityname = req["queryResult"]["parameters"]["cityname"]
        resp_text = getWindIntentHandler(cityname)
    else:
        resp_text = "Unable to find a matching intent. Try again."

    resp = {
        "fulfillmentText": resp_text
    }

    return Response(json.dumps(resp), status=200, content_type="application/json")

app.run(host='0.0.0.0', port=5000, debug=True)