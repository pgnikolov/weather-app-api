# Weather App :earth_americas:	
![Picture](https://github.com/pgnikolov/weather-app-api/blob/main/weather-app-api-pic.jpg)
## Get Real-time, 3-Day or hourly forcast with [WeatherAPI](https://www.weatherapi.com/)

![weatherapi_logo](https://github.com/pgnikolov/weather-app-api/assets/151896883/f200ace4-93dc-4819-bb7f-9c6f6204ed59)

This is a weather application that retrieves real-time weather conditions, 3-day and hourly forcast for any city in the world. It utilizes the Weather API to fetch the data.

### Features

- Enter country and city in the world and get the weather conditions.
- The app uses the geopy library to determine the latitude and longitude for the city entered by the user.
- The app uses the datetime library to adjust the output of the date.
- The app uses the requests library to make an API call to OpenWeatherMap to get the current weather conditions and the five-days forecast
- The app uses json library API response in in the form of json.


### Requirements

- Python 3.x
- Requests library
- datetime
- geopy

### Installation

1. Clone this repository
```shell
git clone https://github.com/your-username/weather-app-api.git
```

2. Install required libraries:
```shell
pip install requests
pip install geopy
pip install datetime
```

### Usage

1. Obtain an API key :key: from [WeatherAPI](https://www.weatherapi.com/). 
2. Replace api_key in *forecast.py* with your actual API key.
3. Run the script:
```shell
python main_weather.py
```
4. The application will ask for city and country:
```
Enter city name: Sofia
Enter country name: Bulgaria
```
5. Select the desired option by entering the corresponding number.
```
1. Check Real-Time Weather
2. Today forcast
3. Tomorrow forcast
4. Day After Tomorrow forcast
5. Hourly Forecast
6. Exit

Enter the number of your choice:
```
* "Check Real-Time Weather" gives the real time weather conditions.
```
Current Weather at Sofia: 
Current condition: Partly cloudy 
Current Temperature: 16.0°C 
Temperature feels like: 16.0°C 
Clouds: 25% 
Humidity: 82% 
Pressure: 1016.0hPa 
Wind: 
	Speed: 19.1Km/h 
	Wind Gust: 26.3Km/h 
	Direction: SE
```
* "Today forcast" will give(Tomorrow and Day after tomorrow have the same output):
```
Weather forcast for Monday 20 May 2024 at Sofia: 
Conditions today: Patchy rain nearby
Max. temperature: 20.0°C 
Average temperature: 14.5°C 
Min. temperature: 10.9°C 
Chance of rain: 95% 
Humidity: 89% 
Sunrice: 05:59 AM
Sunset: 08:48 PM
Wind: 
	Speed: 12.6Km/h
```
* If the UV index is high the app gives a warning. For example:
```
UV Index: 7.0
Warning: UV Index is high. Take precautions such as wearing sunscreen, a hat, and sunglasses,
and reduce exposure to direct sunlight during midday hours (typically between 10 am and 4 pm).
Apply sunscreen with SPF 30+ liberally and reapply every two hours,
or more often if swimming or sweating. Wear sunglasses that block UVA and UVB rays.
```
* In "Hourly Forecast" you can select from 3 options:
```
1. Check Today's Hourly Forecast
2. Check Tomorrow's Hourly Forecast
3. Check Day After Tomorrow's Hourly Forecast
Enter the number of your choice:
```
* The output information about every hour looks like:
```
Hourly Forecast for Tuesday 21 May 2024:
00:00
	Condition: Partly Cloudy 
	Temperature: 10.5°C
	Feels Like: 9.9°C
	Wind: 6.8 Km/h
01:00
	Condition: Partly Cloudy 
	Temperature: 10.2°C
	Feels Like: 9.3°C
	Wind: 7.6 Km/h
02:00
	Condition: Mist
	Temperature: 9.8°C
	Feels Like: 9.0°C
	Wind: 7.2 Km/h
....
```

