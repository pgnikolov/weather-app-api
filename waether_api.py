import requests
from dotenv import load_dotenv
import os

load_dotenv()


class WeatherAPI:
    def fetch_data(self, city, country):
        raise NotImplementedError("Subclasses should implement this method")


class RapidAPIWeather(WeatherAPI):
    def fetch_data(self, city, country):
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
