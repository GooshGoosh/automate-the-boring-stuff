'''
Chapter 16 Project: Fetching Current Weather Data

get_open_weather.py - Prints the weather for a location from the command line.
'''


import sys
import json
import requests


APPID = 'YOUR_APPID_HERE'


def main():
    """Main function to run the program.
    """
    if len(sys.argv) < 2:
        print('Usage: get_open_weather.py <city name>, <2-letter country code>')
        sys.exit(0)
    location = ' '.join(sys.argv[1:])

    # Download the JSON data from OpenWeatherMap.org's API.
    url = f'https://api.openweathermap.org/data/2.5/forecast/daily' \
          f'?q={location}&cnt=3&APPID={APPID} '
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # Uncomment to see the raw JSON text:
    # print(response.text)

    # Load JSON data into a Python variable.
    weather_data = json.loads(response.text)

    # Print weather descriptions.
    w = weather_data['list']
    print(f'Current weather in {location}:')
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])


if __name__ == "__main__":
    main()
