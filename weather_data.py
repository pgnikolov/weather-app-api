from waether_api import WeatherAPI


class WeatherFetcher:
    """
    Fetch data from weather api
    """
    def __init__(self, api: WeatherAPI):
        """
         Args:
                api (WeatherAPI): Instance of WeatherAPI or its subclass.
        """
        self.api = api

    def fetch_data(self, city, country):
        """
            Fetches weather data from the RapidAPI Weather API.
        Args:
            city (str): Name of the city.
            country (str): Name of the country.
        Returns:
            dict or None: Weather data fetched from the API or None if fetch fails.
        """
        return self.api.fetch_data(city, country)


class WeatherDataProcessor:
    """
    Processes raw weather data into structured formats suitable for display.
    """
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def get_forecast_data(self, city, country):
        """
            Retrieves weather forecast data for a specified city and country.
        Args:
            city (str): Name of the city.
            country (str): Name of the country.
        Returns:
            dict or None: Processed weather data or None if fetch fails.
        """
        data = self.fetcher.fetch_data(city, country)
        return data

    def get_hourly_forecast(self, data: dict):
        """
            Extracts hourly forecast data from the provided weather data.
        Args:
            data (dict): Weather data fetched from the API.
        Returns:
            dict: Hourly forecast data organized by hour.
        """
        hourly_data = {}

        for forecast in data.get('forecast', {}).get('forecastday', []):
            for hour_forecast in forecast.get('hour', []):
                hour = hour_forecast['time'].split(' ')[1].split(':')[0]
                hourly_data.setdefault(hour, hour_forecast)

        return hourly_data
