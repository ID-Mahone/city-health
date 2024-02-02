from delivery_distance_calculator import calculate_delivery_distance
from weather_conditions import get_weather_warning_level, handle_weather_conditions

# Example usage:
order_amount = 100
couriers_percentage = 60
orders_per_courier = 3.2
minutes_below_threshold = 35
city = "Berlin"
region = "East"
is_global_tech_emergency = False
optimizer_stops_assigning = False

# Calculate delivery distance
current_radius = calculate_delivery_distance(order_amount, couriers_percentage, orders_per_courier, minutes_below_threshold, city, region, is_global_tech_emergency, optimizer_stops_assigning)

# Fetch weather warning level
warning_level = get_weather_warning_level(city)

# Handle weather conditions
new_radius = handle_weather_conditions(city, warning_level, current_radius)

print(f"The calculated delivery distance with weather conditions is {new_radius} meters.")
