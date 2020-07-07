# API & JSON
# SITE : openweathermap.org
import requests, json

apikey = "Your API"

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

url = api.format(city = "Seoul,KR", key = apikey)

read = requests.get(url)
json_structured_data = json.loads(read.text)

# Custom functions
def define_humidity(humidity) :
    if humidity >= 40 and humidity <= 60 :
       return "쾌적해요 :)" 
    elif humidity <= 39 :
        return "아.. 건조해서 당신의 입술이 터져요."
    elif humidity >= 61 :
        return "으아!!!!!! 찝찝해!!!!!!!!"
    


# Using JSON
print( json_structured_data )
print( "CITY : ", json_structured_data['name'] )
print( "WEATHER KEY : ", json_structured_data['weather'][0]['main'] )
print( "WEATHER TEMP MIN : ", json_structured_data['main']['temp_min']-273.15, "°C" )
print( "WEATHER TEMP MAX : ", json_structured_data['main']['temp_max']-273.15, "°C" )
print( "WEATHER HUM : ", define_humidity(json_structured_data['main']['humidity']) )
