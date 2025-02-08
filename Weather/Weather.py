import matplotlib.pyplot as plt
import requests

city_name = input("Enter the city name: ")
api_key = "8ef0358877f644c5ba433724252501"
base_url = "https://api.weatherapi.com/v1/current.json?"

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10, 20, 30, 40, 50, 60, 70]

def get_api(city_name, api_key):
    complete_url = base_url + "key=" + api_key + "&q=" + city_name + "&aqi=yes"
    #complete_url = complete_url.replace(" ", "")
    #print(complete_url)
    response = requests.get(complete_url)  # Sending the GET request
    if response.status_code == 200:
        data = response.json()
        main = data['current']
        #wind = data['wind']
        weather_data = main['condition']
        #weather_description = weather_data[0]["description"]
        return {
            'temperature': main['temp_c'],
            #'pressure': main['text'],
            'humidity': main['humidity'],
            'weather_description': weather_data['text'],
            'wind_speed': main['wind_kph'],
            'uv': main['uv']
        }
    else:
        return None, None  # Return None if the city is not found
get_api(city_name, api_key)
# Function to display the weather information for the entered city
weather_data = get_api(city_name, api_key)
if weather_data:
    #kelvin_temp = weather_data['temperature']
    #celsius_temp = kelvin_temp - 273.15
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
