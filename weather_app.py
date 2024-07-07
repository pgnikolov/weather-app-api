import datetime
from weather_api import RapidAPIWeather
from weather_data import WeatherFetcher, WeatherDataProcessor
from favourite_cities import FavouriteCities


class WeatherApp:
    """
    This script provides a command-line interface to interact with weather forecast data using the RapidAPI Weather API.
    It allows users to:
    1. Enter a new city and view its weather forecast.
    2. Manage a list of favourite cities for quick access to their weather information.
    3. Display current weather, daily forecasts, and hourly forecasts for selected cities.
    4. Receive UV index warnings based on current conditions.
    Usage:
        Ensure you have a `.env` file in the project directory containing:
        - RAPIDAPI_KEY: Your RapidAPI key for accessing the Weather API.
        - RAPIDAPI_HOST: Hostname for the RapidAPI endpoint.
    Dependencies:
        - python-dotenv: For loading environment variables from the `.env` file.
        - requests: For making HTTP requests to the RapidAPI Weather API.
    """
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def run(self):
        """
        Runs the main menu of the WeatherApp, allowing the user to enter a new city, view favourite cities,
        remove a city from favourites, or exit the application.
        """
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
        """
        Prompts the user to enter a new city and country, fetches the weather data for that city,
        and adds the city to the favourites list if the data is valid.
        """
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
        """
        Displays the list of favourite cities stored in the favourite cities list.
        """
        cities = FavouriteCities.get_cities()
        if cities:
            print("\nFavourite Cities:")
            for index, city in enumerate(cities):
                print(f"{index + 1}. {city}")
        else:
            print("\nNo favourite cities found.")

    def remove_favourite_city(self):
        """
        Prompts the user to select a city from the favourite cities list to remove.

        """
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
        """
            Displays the weather options menu for the user to check various weather forecasts.
        Args:
            city_name (str): The name of the city.
            data (dict): The weather data for the city.
        """
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
        """
            Displays the current weather for the specified city.
        Args:
            city_name (str): The name of the city.
            data (dict): The weather data for the city.
        """
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
        """
            Displays the daily weather forecast for a specified day.
        Args:
            city_name (str): The name of the city.
            data (dict): The weather data for the city.
            day_index (int): The index of the day for the forecast (0 for today, 1 for tomorrow, etc.).
        """
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
        """
            Displays the hourly weather forecast for the specified city.
        Args:
            city_name (str): The name of the city.
            data (dict): The weather data for the city.
        """
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
        """
            Prints a UV warning based on the UV index.
        Args:
            uv_index (int): The UV index.
        """
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
        """
            Returns a formatted date string for the given day offset from today.
        Args:
            day_offset (int): The number of days from today.
        Returns:
            str: The formatted date string.
        """
        return (datetime.date.today() + datetime.timedelta(days=day_offset)).strftime("%A %d %B %Y")


if __name__ == "__main__":
    api = RapidAPIWeather()
    fetcher = WeatherFetcher(api)
    data_processor = WeatherDataProcessor(fetcher)
    app = WeatherApp(data_processor)
    app.run()
