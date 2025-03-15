
import requests

def get_city_code(city):
    """Fetch weather data from an external API."""
    url = f'https://geoapi.qweather.com/v2/city/lookup?location={city}&key=7d95ea74c21544e893c493a94de45f18'
    response = requests.get(url)
    citycode = response.json()['location'][0]['id']
    return citycode

if __name__ == '__main__':
    coderesult = get_city_code('北京')
    print(coderesult)