import requests
from dotenv import load_dotenv
import os

load_dotenv()


class WeatherAPI:
    """
    Manages the interface for fetching weather data from a remote API.
    """

    def fetch_data(self, city, country):
        """
            Abstract method to be implemented by subclasses.
        Args:
            city (str): Name of the city.
            country (str): Name of the country.
        Returns:
            dict or None: Weather data fetched from the API or None if fetch fails.
        """
        raise NotImplementedError("Subclasses should implement this method")


class RapidAPIWeather(WeatherAPI):
    """
    Implements WeatherAPI using the RapidAPI Weather API.
    """

    def fetch_data(self, city, country):
        """
            Fetches weather data from the RapidAPI Weather API.
        Args:
            city (str): Name of the city.
            country (str): Name of the country.
        Returns:
            dict or None: Weather data fetched from the API or None if fetch fails.
        """
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        querystring = {"q": f"{city},{country}", "days": "3"}
        headers = {
            "X-RapidAPI-Key": os.getenv('RAPIDAPI_KEY'),
            "X-RapidAPI-Host": os.getenv('RAPIDAPI_HOST')
        }
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
