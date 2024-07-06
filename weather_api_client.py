import requests


class WeatherAPIClient:
    """
    Handles communication with the weather API.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city_name):
        url = f"{self.base_url}/weather"
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric'
        }
        return self.make_request(url, params)

    def get_forecast(self, city_name):
        url = f"{self.base_url}/forecast"
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric'
        }
        return self.make_request(url, params)

    @staticmethod
    def make_request(self, url, params):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                print("City not found.")
            elif response.status_code == 429:
                print("Error 429 - Too Many Requests.")
            elif response.status_code == 401:
                print("Invalid API key.")
            else:
                print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None