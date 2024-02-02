def calculate_delivery_distance(order_amount, couriers_percentage, orders_per_courier, minutes_below_threshold, city, region, is_global_tech_emergency, optimizer_stops_assigning):
    # Maximum delivery distance
    max_distance = 5000  # in meters

    # Minimum required couriers percentage for maximum distance
    min_required_percentage = 75

    # Maximum orders per courier threshold
    max_orders_per_courier = 3.7

    # Minimum orders per courier threshold to start increasing distance again
    min_orders_per_courier = 2.5

    # Maximum distance when orders per courier exceed the threshold
    max_orders_distance = 1000  # in meters

    # Distance increment after reaching minimum orders per courier threshold for at least 30 minutes
    distance_increment = 250

    # City-specific parameters
    city_params = {
        "BER": {"short_radius_trigger": 4000, "short_radius_switch": 2.5, "large_radius_trigger": 1500, "large_radius_switch": 2.3, "close_trigger": 3.3, "pause_duration": 7 * 24 * 60},  # 1 week pause
        "CGN": {"short_radius_trigger": 4000, "short_radius_switch": 2.7, "large_radius_trigger": 1500, "large_radius_switch": 2.4, "close_trigger": 3.3},
        "FRA": {"short_radius_trigger": 4000, "short_radius_switch": 3.3, "large_radius_trigger": 1500, "large_radius_switch": 3.3, "close_trigger": "close"},
        # ... Add parameters for other cities
    }

    # Check for global tech emergency or optimizer stopping orders for the city
    if is_global_tech_emergency or optimizer_stops_assigning:
        return 0  # Close orders completely

    # Check city-specific parameters
    if city in city_params:
        params = city_params[city]
        if params["short_radius_trigger"] > 0 and orders_per_courier >= params["short_radius_switch"]:
            return 1500  # Switch to a shorter radius
        elif params["large_radius_trigger"] > 0 and orders_per_courier <= params["large_radius_switch"]:
            return 1500  # Switch to a larger radius
        elif params["close_trigger"] == "close" or orders_per_courier >= params["close_trigger"]:
            return 0  # Close orders completely

    # Check if orders per courier are below the minimum threshold to start increasing distance again
    if orders_per_courier <= min_orders_per_courier and minutes_below_threshold >= 30:
        max_distance += distance_increment

    # Check if couriers percentage is less than 50%
    if couriers_percentage < 50:
        max_distance -= 500
    elif couriers_percentage < min_required_percentage:
        # Calculate additional distance reduction for each 5% increase beyond 50%
        additional_reduction = ((min_required_percentage - couriers_percentage) // 5) * 100
        max_distance -= additional_reduction

    return min(max_distance, max_orders_distance)
