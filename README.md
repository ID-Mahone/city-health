# city-health

This code is still under development. The project provides a delivery distance calculation mechanism considering various factors such as order volume, courier availability, and weather conditions. The primary goal is to dynamically adjust the delivery radius based on specific conditions, optimizing the delivery process.

## Features

- **Dynamic Delivery Radius**: Adjusts the delivery radius in real-time based on current operational parameters.
- **Weather Integration**: Incorporates weather conditions to ensure safe and timely deliveries.
- **Courier Management**: Monitors courier availability and workload to maintain efficiency.

## Functionality
calculate_delivery_distance

This function calculates the optimal delivery distance based on the following parameters:

- order_amount: The total number of orders.
- couriers_percentage: The percentage of available couriers.
- orders_per_courier: The average number of orders assigned to each courier.
- minutes_below_threshold: The duration below the minimum orders per courier threshold.
- city: The city for which the delivery distance is calculated.
- region: The region within the city (currently not used).
- is_global_tech_emergency: Flag for a global technical emergency.
- optimizer_stops_assigning: Flag indicating if the optimizer has stopped assigning orders.
- City-Specific Parameters
- The delivery distance calculation is city-specific, with parameters stored in the city_params dictionary. Each city - has its own set of triggers and thresholds for adjusting the delivery radius.

## Weather Conditions

The code utilizes an external API (Deutscher Wetterdienst) to fetch weather warning levels for a given city. Based on the warning level, the handle_weather_conditions function adjusts the delivery radius accordingly.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ID-Mahone/city-health.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd city-health
   ```

3. **Install Dependencies**:

   Ensure you have [Python](https://www.python.org/downloads/) installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:

   ```bash
   python app.py
   ```

2. **Access the Application**:

   Open your browser and navigate to `http://localhost:5000` to interact with the application.


The code relies on the requests library for fetching weather data from the Deutscher Wetterdienst API. Ensure that the library is installed in your environment:

``bash
Copy code

pip install requests

## Configuration

- **Weather API**: To integrate real-time weather data, sign up for an API key from a weather service provider (e.g., [OpenWeatherMap](https://openweathermap.org/api)) and update the `weather_conditions.py` file with your API key.

- **City and Region Data**: Modify the `delivery_distance_calculator.py` file to include specific city and region parameters as needed.


## Notes
The weather API key should be replaced with a valid one from for example "Deutscher Wetterdienst" for accurate weather data retrieval in your region.
City-specific parameters may need adjustments based on real-world data and optimization requirements.
Feel free to customize the code and parameters to suit specific use cases and enhance the delivery distance optimization process.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue in this repository.

---


## Author
David Manning


