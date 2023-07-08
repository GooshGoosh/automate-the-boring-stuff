#!/usr/bin/env python3

# getOpenWeather.py - Prints the weather for a location from the command-line.

APPID = 'YOUR_APPID_HERE'

import json
import requests
import sys


def main():
    # Compute location from command-line arguments.
    if len(sys.argv) < 2:
        print('Usage: getOpenWeather.py <city name>, <2-letter country code>')
        sys.exit()
    location = ' '.join(sys.argv[1:])

    # Download the JSON data from OpenWeatherMap.org's API.
    url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location,
                                                                                           APPID)
    response = requests.get(url)
    response.raise_for_status()

    # Uncomment to see the raw JSON text:
    # print(response.text)

    # Load JSON data into a Python variable.
    weatherData = json.loads(response.text)

    # Print weather descriptions.
    w = weatherData['list']
    print('Current weather in %s:' % (location))
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])


if __name__ == "__main__":
    main()

