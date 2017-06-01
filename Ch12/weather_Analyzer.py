from datetime import datetime, timedelta

import numpy as np

import matplotlib.pyplot as plt

import json
import sys

class WeatherAnalyzer:
    def __init__(self):
        self.data = {}
        self.location_rainfall_list = {}

    def load_json(self, input_file):
        jsonFile = open(input_file, encoding='utf8')
        self.data = json.load(jsonFile)
        jsonFile.close()

    def analyze_data(self):
        for location in self.data:
            print(location)
            self.location_rainfall_list[location] =[]
            monthly_rainfall = 0.0
            current_month = 9
            for hour in self.data[location]:
                dt = self.parse_time(hour['time'])
                if dt.month == current_month:
                    if hour['rainfall'] == 'T':
                        continue
                    monthly_rainfall += float(hour['rainfall'])
                else:
                    self.location_rainfall_list[location].append(monthly_rainfall)
                    current_month += 1
                    if current_month > 12:
                        current_month -= 12
                    monthly_rainfall = 0
                    if hour['rainfall'] == 'T':
                        continue
                    monthly_rainfall += float(hour['rainfall'])
            print(self.location_rainfall_list[location])

    def parse_time(self, time):
        time_format = '%Y-%m-%d %H:%M'
        try:
            dt = datetime.strptime(time, time_format)
            return dt
        except ValueError as e:
            time = time.replace('24','23')
            dt = datetime.strptime(time, time_format)
            dt += timedelta(hours = 1)
            return dt


def main():
    try:
        input_file = sys.argv[1]
    except IndexError as e:
        print("[Usage] python WeatherAnalyzer.py input\\Weather_data.json")
        return
    analyzer = WeatherAnalyzer()
    analyzer.load_json(input_file)
    analyzer.analyze_data()

if __name__ == '__main__':
    main()