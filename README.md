# Weather App ![weatherapi_logo](https://github.com/pgnikolov/weather-app-api/assets/151896883/f200ace4-93dc-4819-bb7f-9c6f6204ed59)
![weather-2789613_640](https://github.com/pgnikolov/weather-app-api/assets/151896883/cb11857d-9403-4d62-a5bb-d15f30322d23)

## Get Real-time, 3-Day or hourly forcast with [WeatherAPI](https://www.weatherapi.com/)



This project provides a command-line interface to interact with weather forecast data using the RapidAPI Weather API. It allows users to fetch and display weather information for various cities, manage a list of favorite cities, and view current, daily, and hourly forecasts.

## Table of Contents 📂

1. Requirements
2. Installation
3. Configuration
4. Usage
    - Running the Application
    - Main Menu Options
    - Weather Options Menu
5. Contributing
6. License
7. Contact

## Requirements 📋
- Python 3.6 or higher
- `python-dotenv`: For loading environment variables from the .env file.
- `requests`: For making HTTP requests to the RapidAPI Weather API.

## Installation ⚙️
1. Clone the repository
```bash
git clone https://github.com/yourusername/weather-forecast-api.git
cd weather-forecast-api
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate 
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the root directory with the following content:
    - Replace your_rapidapi_key with your actual RapidAPI key.
```bash
RAPIDAPI_KEY=your_rapidapi_key
RAPIDAPI_HOST=weatherapi-com.p.rapidapi.com
```

## Configuration 🧰
Ensure you have a `.env` file with your RapidAPI key and host details as described in the Installation section. This file is necessary for the application to authenticate and fetch weather data from the RapidAPI Weather API.

## Usage 💻

### Running the Application ⏯️
To run the Weather Forecast API application, execute the following command:
```bash
python weather_app.py
```

### Main Menu Options 🔢
Once the application is running, you will see the main menu with the following options:
1. ***Enter a new city***: Allows you to enter a new city and country, fetch the weather data for that city, and add it to the favorites list if the data is valid.
2. ***View favorite cities***: Displays the list of favorite cities stored in the favorite cities list.
3. ***Remove a city from favorites***: Allows you to remove a city from the favorites list.
4. ***Exit***: Exits the application.

### Weather Options Menu ⛈️
After entering a new city, you can select from the following weather options:

1. ***Check Current Weather***: Displays the current weather for the specified city.
2. ***Check Today's Forecast***: Displays the weather forecast for today.
3. ***Check Tomorrow's Forecast***: Displays the weather forecast for tomorrow.
4. ***Check Day After Tomorrow's Forecast***: Displays the weather forecast for the day after tomorrow.
5. ***Check Hourly Forecast***: Displays the hourly weather forecast for the specified city.
6. ***Exit***: Returns to the main menu.

1. Obtain an API key :key: from [WeatherAPI](https://www.weatherapi.com/). 


## Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

## License 📝
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
