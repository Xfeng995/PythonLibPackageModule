import sys
from .fetcher import get_weather
from .parser import parse_weather
from .formatter import format_output
from .fetchercitycode import get_city_code

if len(sys.argv) != 2:
    print("Usage: python cli.py <city>")
    sys.exit(1)

city = sys.argv[1]
citycode = get_city_code(city)
data = get_weather(citycode)
location, temp_c, condition = parse_weather(data)
output = format_output(location, temp_c, condition)
print(output)