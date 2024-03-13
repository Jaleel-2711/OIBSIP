import requests

def fetch_weather(city):
    api_key = "ced5b2ee86f80f503439d8f3b684bca5"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] == 200:
            return data
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"Error fetching weather data: {e}")

def display_weather(data):
    if data:
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_desc}")
    else:
        print("No weather data available.")

def main():
    city = input("Enter city name: ")
    weather_data = fetch_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
