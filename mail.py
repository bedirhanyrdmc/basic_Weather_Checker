import requests

apikey = "Copy and paste your API key here"
city_name = input("Enter the city name =")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apikey}")
if weather_data.status_code != 200:  
    print("City could not found or API error")
else:
    #print(weather_data.content)
    print("City name -->",city_name)
    weather_desctiption = weather_data.json()["weather"][0]["main"]
    temperature_Kelvin = weather_data.json()["main"]["temp"] 
    temperature_F= (temperature_Kelvin-273.15)*9/5+32
    print("Weather Description -->",weather_desctiption)
    print(f"Temperature --> {temperature_F:.2f}")
