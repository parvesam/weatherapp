import requests

API_KEY = ""  # WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/current.json"

print("🌦️ Welcome to the Weather Info App!\n")

while True:
    city = input("Enter a city name (or type 'exit' to quit): ")
    if city.lower() == "exit":
        break

    try:
        params = {
            "key": API_KEY,
            "q": city,
            "aqi": "no"
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]

        print(f"\n🌍 Weather in {location}, {country}:")
        print(f"🌡️ Temperature: {temp_c}°C")
        print(f"🌤️ Condition: {condition}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_kph} km/h\n")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP Error: {http_err}")
    except Exception as err:
        print(f"❌ An error occurred: {err}")
