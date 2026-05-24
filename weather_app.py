import requests
API_KEY = "8905fa9007656def5990497ed0278c9a"
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
try:
    response = requests.get(url)
    data = response.json()
    print(data)   
    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        print("\nWeather Report")
        print("----------------")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", condition)
    else:
        print("Error:", data["message"])
except Exception as e:
    print("Something went wrong:", e)