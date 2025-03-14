import requests

def get_weather(city):
    """Fetch weather data from an external API."""
    url = f'https://devapi.qweather.com/v7/weather/now?key=7d95ea74c21544e893c493a94de45f18&location={city}'
    response = requests.get(url)
    return response.json()