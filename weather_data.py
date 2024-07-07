from waether_api import WeatherAPI


class WeatherFetcher:
    def __init__(self, api: WeatherAPI):
        self.api = api

    def fetch_data(self, city, country):
        return self.api.fetch_data(city, country)


class WeatherDataProcessor:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def get_forecast_data(self, city, country):
        data = self.fetcher.fetch_data(city, country)
        return data

    def get_hourly_forecast(self, data: dict):
        hourly_data = {}

        for forecast in data.get('forecast', {}).get('forecastday', []):
            for hour_forecast in forecast.get('hour', []):
                hour = hour_forecast['time'].split(' ')[1].split(':')[0]
                hourly_data.setdefault(hour, hour_forecast)

        return hourly_data
