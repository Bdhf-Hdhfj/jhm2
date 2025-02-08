import matplotlib.pyplot as plt
import requests

city_name = input("Enter the city name: ")
api_key = "8ef0358877f644c5ba433724252501"
base_url = "https://api.weatherapi.com/v1/current.json?"

def get_api(city_name, api_key):
    complete_url = base_url + "key=" + api_key + "&q=" + city_name + "&aqi=yes"
    response = requests.get(complete_url)  
    if response.status_code == 200:
        data = response.json()
        main = data['current']
        weather_data = main['condition']
        return {
            'temperature': main['temp_c'],
            'humidity': main['humidity'],
            'weather_description': weather_data['text'],
            'wind_speed': main['wind_kph'],
            'uv': main['uv']
        }
    else:
        return None, None  
get_api(city_name, api_key)
weather_data = get_api(city_name, api_key)
if weather_data:
    print("Weather Data for", city_name, ":")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Temperature: {weather_data['temperature']}˚C")
    print(f"Wind Speed: {weather_data['wind_speed']} km/h")
    print(f"Condition: {weather_data['weather_description']}")
    print(f"UV Index: {weather_data['uv']}")
    weather__data = ['Temperature(˚C)', 'Humidity(%)', 'Wind Speed(km/h)', 'UV Index']
    Values = [weather_data['temperature'], weather_data['humidity'], weather_data['wind_speed'], weather_data['uv']]
    plt.bar(weather__data, Values, color='skyblue')
    plt.title("Weather Parameters Visualization") 
    plt.ylabel("Values")    
    plt.show()
    plt.savefig("Weather_Parameters_Visualization.png")  
    print("圖表已儲存為 Weather_Parameters_Visualization.png")
else:
    print("City Not Found")
