import requests

def get_weather_warning_level(city):
    # Replace 'your_api_key' with the actual API key obtained from Deutscher Wetterdienst
    api_key = 'your_api_key'
    base_url = 'https://dwd.api.bund.dev/openweather/v1/warnings/'

    try:
        response = requests.get(f'{base_url}{city}?apiKey={api_key}')
        data = response.json()
        warning_level = data.get('level', 0)
        return warning_level
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return 0

def handle_weather_conditions(city, warning_level, current_radius):
    if warning_level == 1 or warning_level == 2:
        # Operate as usual
        return current_radius
    elif warning_level == 3:
        # Short-lived severe weather events
        # For simplicity, let's assume that we always reduce the radius to 3000 meters
        print("Reducing radius to 3000 due to severe weather (Level 3)")
        return 3000
    elif warning_level == 4:
        # Extreme weather, close deliveries
        print("Closing deliveries due to extreme weather (Level 4)")
        return 0  # Close deliveries completely
    else:
        return current_radius  # Default behavior
