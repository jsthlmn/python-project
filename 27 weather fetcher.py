import requests

# have to generate API KEY before run this program
API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature =  round(data['main']['temp'] - 273.15, 2)

    print("City: ", city)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "Celcius")
else:
    print("An error occured")