import sys
from weather_tool import fetcher
from weather_tool import parser
from weather_tool import formatter
from weather_tool import fetchercitycode

if len(sys.argv) != 2:
    print("Usage: python getweather.py <city>")
    sys.exit(1)
city = sys.argv[1]
# city = '长春'
citycode = fetchercitycode.get_city_code(city)
data = fetcher.get_weather(citycode)
location, temp_c, condition = parser.parse_weather(city, data)
output = formatter.format_output(location, temp_c, condition)
print(output)