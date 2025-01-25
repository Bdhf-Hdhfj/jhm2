import requests
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        return {
            'temperature': main['temp'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'weather_description': weather['description'],
            'wind_speed': wind['speed']
        }
    else:
        return None
api_key = "b4b06b5a9d56c561bb31f43a6e170bf3"
city_name = "London"
weather_data = get_weather(city_name, api_key)
if weather_data:
    print(f"Temperature: {weather_data['temperature']}")
    print(f"Pressure: {weather_data['pressure']}")
    print(f"Humidity: {weather_data['humidity']}")
    print(f"Weather Description: {weather_data['weather_description']}")
    print(f"Wind Speed: {weather_data['wind_speed']}")
else:
    print("City Not Found")