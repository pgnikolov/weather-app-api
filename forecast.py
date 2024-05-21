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
