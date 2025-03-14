def parse_weather(location, data):
    """Parse weather data to extract relevant information."""
    # location = data['location']['name']
    location = location
    temp_c = data['now']['temp']
    condition = data['now']['text']
    return location, temp_c, condition