from datetime import datetime


class WeatherData:
    """
    Represents weather data received from the weather API.
    """

    @staticmethod
    def get_wind_direction(degrees):
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
        idx = round(degrees / 45) % 8
        return directions[idx]

    @staticmethod
    def print_current_weather(data):
        if data:
            sunrise_time = datetime.fromtimestamp(data['sys']['sunrise']).strftime("%H:%M:%S")
            sunset_time = datetime.fromtimestamp(data['sys']['sunset']).strftime("%H:%M:%S")
            wind_direction = WeatherData.get_wind_direction(data['wind']['deg'])
            print(f'Current Weather at {data["name"].capitalize()}: \n'
                  f'{data["weather"][0]["description"].capitalize()} \n'
                  f'Current Temperature: {data["main"]["temp"]}°C \n'
                  f'Temperature feels like: {data["main"]["feels_like"]}°C \n'
                  f'Max Temperature: {data["main"]["temp_max"]}°C \n'
                  f'Min Temperature: {data["main"]["temp_min"]}°C \n'
                  f'Sunrise: {sunrise_time} \n'
                  f'Sunset: {sunset_time} \n'
                  f'Humidity: {data["main"]["humidity"]}% \n'
                  f'Pressure: {data["main"]["pressure"]}hPa \n'
                  f'Visibility: {data["visibility"] / 1000:.2f}Km \n'
                  f'Wind: {data["wind"]["speed"] * 3.6:.2f}Km/h {wind_direction}')
        else:
            print("No data to display.")

    @staticmethod
    def print_forecast(data):
        if data:
            daily_forecasts = {}
            for entry in data["list"]:
                date = entry["dt_txt"].split()[0]
                if date not in daily_forecasts:
                    daily_forecasts[date] = {"descriptions": [], "temps": []}
                daily_forecasts[date]["descriptions"].append(entry["weather"][0]["description"])
                daily_forecasts[date]["temps"].append(entry["main"]["temp"])

            for date, forecast in daily_forecasts.items():
                avg_temp = round(sum(forecast["temps"]) / len(forecast["temps"]), 1)
                descriptions = ", ".join(set(forecast["descriptions"]))
                print(f"\n- {date}:")
                print(f"  Descriptions: {descriptions}")
                print(f"  Average Temp: {avg_temp}°C")
        else:
            print("No data to display.")
