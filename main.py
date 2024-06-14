import datetime
import requests
import geopy.geocoders as geocoders


def get_forcast_data(city, country):
    # Combine city and country for geocoding
    location_string = f"{city}, {country}"

    locator = geocoders.Nominatim(user_agent="my_app")  # Replace with your app name

    location = locator.geocode(location_string)

    if not location:
        print(f"Location not found for {location_string}")
        return None

    latitude = location.latitude
    longitude = location.longitude
    use_loc = f"{latitude},{longitude}"

    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q": f"{use_loc}", "days": "3"}

    headers = {
        "X-RapidAPI-Key": "{api_key}",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    r = requests.get(url, headers=headers, params=querystring)

    data = r.json()

    return data


def get_hour_forecast(data: dict):

    hourly_data = {}

    for forecast in data:
        # take the hour from the "time" string
        hour = forecast['time'].split(' ')[1].split(':')[0]

        # If the hour doesn't't exist as a key in the dictionary, create it
        if hour not in hourly_data:
            hourly_data[hour] = {}

        # Update the hourly data with the current forecast
        hourly_data[hour] = forecast

    return hourly_data


def print_hourly_forecast(hourly_data, date):
    print(f"\nHourly Forecast for {date}:")
    for hour, forecast in hourly_data.items():
        print(f"{hour}:00")
        print(f"\tCondition: {forecast['condition']['text']}")
        print(f"\tTemperature: {forecast['temp_c']}°C")
        print(f"\tFeels Like: {forecast['feelslike_c']}°C")
        print(f"\tWind: {forecast['wind_kph']} Km/h")


def uv_warning(uv_index):
    if uv_index >= 11:
        print("There is an extreme risk of harm from UV rays. Try to avoid sun exposure during peak sunlight\n"
              "hours (typically between 10 am and 4 pm). If you must be outdoors, cover up as much skin as\n"
              "possible with sun-protective clothing. Apply sunscreen with SPF 50+ liberally and reapply every\n"
              "two hours, or more often if swimming or sweating. Wear sunglasses that block UVA and UVB rays.\n")
    elif 9 <= uv_index < 11:
        print("There is a very high risk of harm from UV rays. Limit time outdoors, especially during peak\n"
              "sunlight hours (typically between 10 am and 4 pm).Cover up as much skin as possible\n"
              "with sun-protective clothing. Apply sunscreen with SPF 50+ liberally and reapply every two hours\n,"
              "or more often if swimming or sweating. Wear sunglasses that block UVA and UVB rays.\n")
    elif 6 <= uv_index < 9:
        print("Warning: UV Index is high. Take precautions such as wearing sunscreen, a hat, and sunglasses,\n"
              "and reduce exposure to direct sunlight during midday hours (typically between 10 am and 4 pm).\n"
              "Apply sunscreen with SPF 30+ liberally and reapply every two hours,\n"
              "or more often if swimming or sweating. Wear sunglasses that block UVA and UVB rays.\n")


# HANDLE INCORECT INPUT
while True:
    city_name = input('Enter city name: ')
    country_name = input('Enter country name: ')

    data = get_forcast_data(city_name, country_name)

    if data:
        break
    else:
        print("Invalid city or country. Please try again.")

today_date = datetime.date.today().strftime("%A %d %B %Y")

realtime = {
    # (REALTIME WEATHER) : temp-°C, temp_feel-°C, wind_speed-km/h, wind_direction - East West,
    # condition - result as clouds, sun, humidity - % , wind_gust-km/h, last_updated as date, pressure-hPa,
    # precip_mm = rains as mm , clouds = c['cloud']  # clouds as % uv_index - UV index (see uv-index pic)
    "temp": data['current']['temp_c'],
    "feelslike": data['current']['feelslike_c'],
    "wind_kph": data['current']['wind_kph'],
    "wind_direction": data['current']['wind_dir'],
    "condition": data['current']['condition']['text'],
    "humidity": data['current']['humidity'],
    "wind_gust": data['current']['gust_kph'],
    "last_updated": data['current']['last_updated'],
    "pressure": data['current']['pressure_mb'],
    "precip_mm": data['current']['precip_mm'],
    "cloud": data['current']['cloud'],
    "uv_index": data['current']['uv']
}

tday = data['forecast']['forecastday'][0]

today = {
    'daily': {
        'date': datetime.date.today().strftime("%A %d %B %Y"),
        'sunrise': tday['astro']['sunrise'],
        'sunset': tday['astro']['sunset'],
        "maxtemp": tday['day']['maxtemp_c'],
        "mintemp": tday['day']['mintemp_c'],
        "avgtemp": tday['day']['avgtemp_c'],
        "maxwind_kph": tday['day']['maxwind_kph'],
        "condition": tday['day']['condition']['text'],
        "avghumidity": tday['day']['avghumidity'],
        "totalprecip_mm": tday['day']['totalprecip_mm'],
        "totalsnow_cm": tday['day']['totalsnow_cm'],
        "chance_of_rain": tday['day']['daily_chance_of_rain'],
        "chance_of_snow": tday['day']['daily_chance_of_snow'],
        "uv_index": tday['day']['uv']
    },
    # HOURLY VALUES
    # 'time': '2024-05-20 00:00', 'temp_c': 10.8, 'condition': {'text': 'Mist'}, 'wind_kph': 6.8,  'wind_dir': 'ESE',
    # 'pressure_mb': 1015.0, 'precip_mm': 0.0, 'snow_cm': 0.0, 'humidity': 94, 'cloud': 67, 'feelslike_c': 10.2,
    # 'windchill_c': 10.2, 'heatindex_c': 10.8, 'dewpoint_c': 9.9, chance_of_rain': 0,'chance_of_snow': 0, 'vis_km': 2.0
    # 'gust_kph': 13.4, 'uv': 1.0
    "hourly": get_hour_forecast(tday['hour'])  # today['hourly']['00'] = today 00:00
}

trow = data['forecast']['forecastday'][1]
tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)

tomorrow = {
    'daily': {
        'date': tomorrow_date.strftime("%A %d %B %Y"),
        'sunrise': trow['astro']['sunrise'],
        'sunset': trow['astro']['sunset'],
        "maxtemp": trow['day']['maxtemp_c'],
        "mintemp": trow['day']['mintemp_c'],
        "avgtemp": trow['day']['avgtemp_c'],
        "maxwind_kph": trow['day']['maxwind_kph'],
        "condition": trow['day']['condition']['text'],
        "avghumidity": trow['day']['avghumidity'],
        "totalprecip_mm": trow['day']['totalprecip_mm'],
        "totalsnow_cm": trow['day']['totalsnow_cm'],
        "chance_of_rain": trow['day']['daily_chance_of_rain'],
        "chance_of_snow": trow['day']['daily_chance_of_snow'],
        "uv_index": trow['day']['uv']
    },
    'hourly': get_hour_forecast(trow['hour'])  # today['hourly']['00'] = today 00:00
}

datrow = data['forecast']['forecastday'][2]  # Day after tomorrow
day_after_trow_date = datetime.date.today() + datetime.timedelta(days=2)

day_after_tomorrow = {
    'daily': {
        'date': day_after_trow_date.strftime("%A %d %B %Y"),
        'sunrise': datrow['astro']['sunrise'],
        'sunset': datrow['astro']['sunset'],
        "maxtemp": datrow['day']['maxtemp_c'],
        "mintemp": datrow['day']['mintemp_c'],
        "avgtemp": datrow['day']['avgtemp_c'],
        "maxwind_kph": datrow['day']['maxwind_kph'],
        "condition": datrow['day']['condition']['text'],
        "avghumidity": datrow['day']['avghumidity'],
        "totalprecip_mm": datrow['day']['totalprecip_mm'],
        "totalsnow_cm": datrow['day']['totalsnow_cm'],
        "chance_of_rain": datrow['day']['daily_chance_of_rain'],
        "chance_of_snow": datrow['day']['daily_chance_of_snow'],
        "uv_index": datrow['day']['uv']
    },
    'hourly': get_hour_forecast(trow['hour'])  # today['hourly']['00'] = today 00:00
}

while True:
    print("1. Check Real-Time Weather")
    print("2. Today forcast")
    print("3. Tomorrow forcast")
    print("4. Day After Tomorrow forcast")
    print("5. Hourly Forecast")
    print("6. Exit\n")

    user_choice = input("Enter the number of your choice: \n")

    if user_choice == '1':
        print(f'Current Weather at {city_name.capitalize()}: \n'
              f'Current condition: {realtime["condition"].capitalize()} \n'
              f'Current Temperature: {realtime["temp"]}°C \n'
              f'Temperature feels like: {realtime["feelslike"]}°C \n'
              f'Clouds: {realtime["cloud"]}% \n'
              f'Humidity: {realtime["humidity"]}% \n'
              f'Pressure: {realtime["pressure"]}hPa \n'
              f'Wind: \n'
              # wind speed ot m/s v km/h - \t - 4 spaces
              f'\tSpeed: {realtime["wind_kph"]}Km/h \n'
              f'\tWind Gust: {realtime["wind_gust"]}Km/h \n'
              f'\tDirection: {realtime["wind_direction"]}\n')
        if int(realtime["uv_index"]) >= 6:
            print(f"UV Index: {realtime['uv_index']}")
            uv_warning(realtime["uv_index"])

    elif user_choice == "2":

        print(f"Weather forcast for {today['daily']['date']} at {city_name.capitalize()}: \n"
              f"Conditions today: {today['daily']['condition']}\n"
              f"Max. temperature: {today['daily']['maxtemp']}°C \n"
              f"Average temperature: {today['daily']['avgtemp']}°C \n"
              f"Min. temperature: {today['daily']['mintemp']}°C \n"
              f"Chance of rain: {today['daily']['chance_of_rain']}% \n"
              f"Humidity: {today['daily']['avghumidity']}% \n"
              f"Sunrice: {today['daily']['sunrise']}\n"
              f"Sunset: {today['daily']['sunset']}\n"
              f'Wind: \n'
              # wind speed ot m/s v km/h - \t - 4 spaces
              f"\tSpeed: {today['daily']['maxwind_kph']}Km/h \n")
        if int(today['daily']["uv_index"]) >= 6:
            print(f"UV Index: {today['daily']['uv_index']}")
            uv_warning(today['daily']["uv_index"])

    elif user_choice == "3":

        print(f"Weather forcast for {tomorrow['daily']['date']} at {city_name.capitalize()}: \n"
              f"Conditions: {tomorrow['daily']['condition']}\n"
              f"Max. temperature: {tomorrow['daily']['maxtemp']}°C \n"
              f"Average temperature: {tomorrow['daily']['avgtemp']}°C \n"
              f"Min. temperature: {tomorrow['daily']['mintemp']}°C \n"
              f"Chance of rain: {tomorrow['daily']['chance_of_rain']}% \n"
              f"Humidity: {tomorrow['daily']['avghumidity']}% \n"
              f"Sunrice: {tomorrow['daily']['sunrise']}\n"
              f"Sunset: {tomorrow['daily']['sunset']}\n"
              f'Wind: \n'
              # wind speed ot m/s v km/h - \t - 4 spaces
              f"\tSpeed: {tomorrow['daily']['maxwind_kph']}Km/h \n")
        if int(tomorrow['daily']["uv_index"]) >= 6:
            print(f"UV Index: {tomorrow['daily']['uv_index']}")
            uv_warning(tomorrow['daily']["uv_index"])

    elif user_choice == "4":

        print(f"Weather forcast for {day_after_tomorrow['daily']['date']} at {city_name.capitalize()}: \n"
              f"Conditions: {day_after_tomorrow['daily']['condition']}\n"
              f"Max. temperature: {day_after_tomorrow['daily']['maxtemp']}°C \n"
              f"Average temperature: {day_after_tomorrow['daily']['avgtemp']}°C \n"
              f"Min. temperature: {day_after_tomorrow['daily']['mintemp']}°C \n"
              f"Chance of rain: {day_after_tomorrow['daily']['chance_of_rain']}% \n"
              f"Humidity: {day_after_tomorrow['daily']['avghumidity']}% \n"
              f"Sunrice: {day_after_tomorrow['daily']['sunrise']}\n"
              f"Sunset: {day_after_tomorrow['daily']['sunset']}\n"
              f'Wind: \n'
              # wind speed ot m/s v km/h - \t - 4 spaces
              f"\tSpeed: {day_after_tomorrow['daily']['maxwind_kph']}Km/h \n")
        if int(day_after_tomorrow['daily']["uv_index"]) >= 6:
            print(f"UV Index: {day_after_tomorrow['daily']['uv_index']}")
            uv_warning(day_after_tomorrow['daily']["uv_index"])

    elif user_choice == "5":
        print("\n1. Check Today's Hourly Forecast")
        print("2. Check Tomorrow's Hourly Forecast")
        print("3. Check Day After Tomorrow's Hourly Forecast")

        user_choice = input("Enter the number of your choice: \n")

        if user_choice == '1':
            print_hourly_forecast(today['hourly'], today_date)

        elif user_choice == "2":
            if len(data['forecast']['forecastday']) > 1:
                print_hourly_forecast(tomorrow['hourly'], tomorrow['daily']['date'])
            else:
                print(f"Hourly data for tomorrow ({tomorrow['daily']['date']}) might not be available")

        elif user_choice == "3":
            if len(data['forecast']['forecastday']) > 2:
                print_hourly_forecast(day_after_tomorrow['hourly'], day_after_tomorrow['daily']['date'])
            else:
                print(f"Hourly data for day after tomorrow {day_after_tomorrow['daily']['date']} might not be available")

        else:
            print("Invalid choice")

    elif user_choice == "6":
        break
