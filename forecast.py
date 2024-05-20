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

        # If the hour doesn''t exist as a key in the dictionary, create it
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

