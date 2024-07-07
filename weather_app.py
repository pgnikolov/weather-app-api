import datetime
from waether_api import RapidAPIWeather
from weather_data import WeatherFetcher, WeatherDataProcessor
from favourite_cities import FavouriteCities


class WeatherApp:
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def run(self):
        while True:
            print("\n1. Enter a new city")
            print("2. View favourite cities")
            print("3. Remove a city from favourites")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.new_city_weather()
            elif choice == '2':
                self.view_favourite_cities()
            elif choice == '3':
                self.remove_favourite_city()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

    def new_city_weather(self):
        city_name = input('Enter city name: ')
        country_name = input('Enter country name: ')
        data = self.data_processor.get_forecast_data(city_name, country_name)
        if data:
            FavouriteCities.add_city(city_name)
            self.print_menu(city_name, data)
        else:
            print("Invalid city or country. Please try again.")

    @ staticmethod
    def view_favourite_cities():
        cities = FavouriteCities.get_cities()
        if cities:
            print("\nFavourite Cities:")
            for index, city in enumerate(cities):
                print(f"{index + 1}. {city}")
        else:
            print("\nNo favourite cities found.")

    def remove_favourite_city(self):
        cities = FavouriteCities.get_cities()
        if cities:
            self.view_favourite_cities()
            try:
                city_index = int(input("\nEnter the number of the city to remove: ")) - 1
                FavouriteCities.remove_city(city_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("No favourite cities to remove.")

    def print_menu(self, city_name, data):
        while True:
            print("\n1. Check Current Weather")
            print("2. Check Today's Forecast")
            print("3. Check Tomorrow's Forecast")
            print("4. Check Day After Tomorrow's Forecast")
            print("5. Check Hourly Forecast")
            print("6. Exit")

            user_choice = input("Enter the number of your choice: ")

            if user_choice == '1':
                self.show_current_weather(city_name, data)
            elif user_choice == '2':
                self.show_daily_forecast(city_name, data, 0)
            elif user_choice == '3':
                self.show_daily_forecast(city_name, data, 1)
            elif user_choice == '4':
                self.show_daily_forecast(city_name, data, 2)
            elif user_choice == '5':
                self.show_hourly_forecast(city_name, data)
            elif user_choice == '6':
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

    def show_current_weather(self, city_name, data):
        current_data = {
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

        print(f'\nCurrent Weather in {city_name.capitalize()}:')
        print(f'Condition: {current_data["condition"].capitalize()}')
        print(f'Temperature: {current_data["temp"]}°C')
        print(f'Feels Like: {current_data["feelslike"]}°C')
        print(f'Clouds: {current_data["cloud"]}%')
        print(f'Humidity: {current_data["humidity"]}%')
        print(f'Pressure: {current_data["pressure"]} hPa')
        print(f'Wind:')
        print(f'  Speed: {current_data["wind_kph"]} km/h')
        print(f'  Wind Gust: {current_data["wind_gust"]} km/h')
        print(f'  Direction: {current_data["wind_direction"]}')

        if int(current_data["uv_index"]) >= 6:
            self.uv_warning(current_data["uv_index"])

    def show_daily_forecast(self, city_name, data, day_index):
        forecast_day = data['forecast']['forecastday'][day_index]['day']

        print(f'\nWeather Forecast for {self.get_date(day_index)} in {city_name.capitalize()}:')
        print(f'Condition: {forecast_day["condition"]["text"]}')
        print(f'Max Temperature: {forecast_day["maxtemp_c"]}°C')
        print(f'Average Temperature: {forecast_day["avgtemp_c"]}°C')
        print(f'Min Temperature: {forecast_day["mintemp_c"]}°C')
        print(f'Chance of Rain: {forecast_day["daily_chance_of_rain"]}%')
        print(f'Humidity: {forecast_day["avghumidity"]}%')

        if int(forecast_day["uv"]) >= 6:
            self.uv_warning(forecast_day["uv"])

    def show_hourly_forecast(self, city_name, data):
        hourly_data = self.data_processor.get_hourly_forecast(data)

        print(f'\nHourly Forecast for {self.get_date(0)} in {city_name.capitalize()}:')

        for hour, forecast in hourly_data.items():
            print(f'{hour}:00')
            print(f'  Condition: {forecast["condition"]["text"]}')
            print(f'  Temperature: {forecast["temp_c"]}°C')
            print(f'  Feels Like: {forecast["feelslike_c"]}°C')
            print(f'  Wind: {forecast["wind_kph"]} km/h')

    @staticmethod
    def uv_warning(uv_index):
        if uv_index >= 11:
            print("There is an extreme risk of harm from UV rays. Try to avoid sun exposure during peak sunlight "
                  "hours (typically between 10 am and 4 pm). If you must be outdoors, cover up as much skin as "
                  "possible with sun-protective clothing. Apply sunscreen with SPF 50+ liberally and reapply every "
                  "two hours, or more often if swimming or sweating. Wear sunglasses that block UVA and UVB rays.\n")
        elif 9 <= uv_index < 11:
            print("There is a very high risk of harm from UV rays. Limit time outdoors, especially during peak "
                  "sunlight hours (typically between 10 am and 4 pm). Cover up as much skin as possible "
                  "with sun-protective clothing. Apply sunscreen with SPF 50+ liberally and reapply every two hours, "
                  "or more often if swimming or sweating. Wear sunglasses that block UVA and UVB rays.\n")
        elif 6 <= uv_index < 9:
            print("Warning: UV Index is high. Take precautions such as wearing sunscreen, a hat, and sunglasses, "
                  "and reduce exposure to direct sunlight during midday hours (typically between 10 am and 4 pm). "
                  "Apply sunscreen with SPF 30+ liberally and reapply every two hours, "
                  "or more often if swimming or sweating. Wear sunglasses that block UVA and UVB rays.\n")

    @staticmethod
    def get_date(day_offset):
        return (datetime.date.today() + datetime.timedelta(days=day_offset)).strftime("%A %d %B %Y")


if __name__ == "__main__":
    api = RapidAPIWeather()
    fetcher = WeatherFetcher(api)
    data_processor = WeatherDataProcessor(fetcher)
    app = WeatherApp(data_processor)
    app.run()
