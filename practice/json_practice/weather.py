import json
from datetime import datetime,timedelta

class Weather:
    def __init__(self):
        self.data ={}
        self.location_rainfall_list = {}

    def json_load(self):
        jsonFile = open("weather.json")
        self.data = json.load(jsonFile)
        jsonFile.close()

    def weather_analyze(self):
        for location in self.data:
            print(location)
            self.location_rainfall_list[location] = []
            month_rainfall = 0.0
            current_month = 5

            for hour in self.data[location]:
                dt = self.parse_time(hour['time']) #將hour['time']傳到parse_time中

                if dt.month == current_month:
                    if hour['rainfall'] == "T":
                        continue
                    month_rainfall += float(hour['rainfall'])

                else:
                    self.location_rainfall_list[location].append(month_rainfall) 
                    #在月份轉換時將上次月份的統計資料加進list最後一筆，但是會使得list中最後一個月份的統計資料會無法加進去
                    current_month += 1
                    if current_month > 12:
                        current_month -= 12
                    month_rainfall = 0
                    if hour['rainfall'] == 'T':
                        continue

                    month_rainfall += float(hour['rainfall'])
            print(self.location_rainfall_list[location])


    def parse_time(self,time):          #接收來自self.data裡的time key
        time_format = '%Y-%m-%d %H:%M'  #定義時間格式
        try:
            dt = datetime.strptime(time,time_format)  #將接收到的time字串轉換成時間格式
            return dt
        except ValueError as e:                       #因為時間表示式0~23，但資料裡面有24，所以要寫例外處理
            time = time.replace('24','23')            #將時間字串中的24取代成23
            dt = datetime.strptime(time,time_format)  #在將字串轉換成時間格式
            dt += timedelta(hours = 1)                #因為之前有將時間減1，故在這邊要將時間加回去
            return dt








def main():
    analyzer = Weather()
    analyzer.json_load()
    analyzer.weather_analyze()

if __name__ == '__main__':
    main()