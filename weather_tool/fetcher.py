import requests

def get_weather(citycode):
    """Fetch weather data from an external API."""
    url = f'https://devapi.qweather.com/v7/weather/now?key=7d95ea74c21544e893c493a94de45f18&location={citycode}'
    response = requests.get(url)
    return response.json()