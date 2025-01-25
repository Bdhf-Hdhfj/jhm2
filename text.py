import matplotlib.pyplot as plt
import requests

city_name = input("Enter the city name: ")
api_key = "b4b06b5a9d56c561bb31f43a6e170bf3"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10, 20, 30, 40, 50, 60, 70]

def get_api(city_name, api_key):
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    complete_url = complete_url.replace(" ", "")
    print(complete_url)
    response = requests.get(complete_url)  # Sending the GET request
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_data = data['weather'][0]
        #weather_description = weather_data[0]["description"]
        return {
            'temperature': main['temp'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'weather_description': weather_data['description'],
            'wind_speed': wind['speed']
        }
    else:
        return None, None  # Return None if the city is not found
get_api(city_name, api_key)
# Function to display the weather information for the entered city
weather_data = get_api(city_name, api_key)
if weather_data:
    kelvin_temp = weather_data['temperature']
    celsius_temp = kelvin_temp - 273.15
    celsius_temp = round(celsius_temp, 1)
    print(f"Temperature: {celsius_temp}˚C")
    print(f"Pressure: {weather_data['pressure']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Condition: {weather_data['weather_description']}")
    print(f"Wind Speed: {weather_data['wind_speed']} km/h")
else:
    print("City Not Found")
#show_city(event=None)
#plt.bar(months, sales, color='skyblue')
#plt.title("Product Revenue")  # 圖表標題
#plt.xlabel("Product")         # X 軸標籤
#plt.ylabel("Revenue ($)")     # Y 軸標籤
#plt.show()
#plt.savefig("T1monthly_sales.png")  # 儲存到檔案
#print("圖表已儲存為 T1monthly_sales.png")