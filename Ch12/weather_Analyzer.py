from datetime import datetime, timedelta    #轉換時間使用
import numpy as np                     #生成陣列使用
import matplotlib.pyplot as plt             #用來畫圖
import json

class WeatherAnalyzer:
    def __init__(self):                     #初始化資料
        self.data = {}                      #用來裝data的dict
        self.location_rainfall_list = {}    #用來裝統計資料的dict

    def load_json(self ):
        jsonFile = open('input\weather_data.json')
        self.data = json.load(jsonFile)
        jsonFile.close()

    def analyze_data(self):
        for location in self.data:
            print(location)
            self.location_rainfall_list[location] =[]   #利用location在self.location_raifall_list dict中創一個空list
            monthly_rainfall = 0.0                      #用來統計月降雨量
            current_month = 9                           #因為資料中是從9月開始，故將current_month設為9
            for hour in self.data[location]:            #讀取每地區中的資料，放到hour中
                dt = self.parse_time(hour['time'])      #將hour['time']傳到parse_time中
                if dt.month == current_month:
                    if hour['rainfall'] == 'T':         #因為rainfall中有T這個數值(代表降雨量低於0.1)，故將視為0直接跳過此筆資料
                        continue
                    monthly_rainfall += float(hour['rainfall']) #將此筆資料轉換為float，來進行加總(原本為str)
                else:
                    self.location_rainfall_list[location].append(monthly_rainfall)
                    #在月份轉換時將上次月份的統計資料加進list最後一筆，但是會使得list中最後一個月份的統計資料會無法加進去
                    #故只會統計到2015/9月到2016/8月，2016/9月的資訊不會統計到

                    current_month += 1      #因為是list，所以按照順序+1即可

                    if current_month > 12:  #如果跑到隔年的1月，則將月份-12， 來得到1月
                        current_month -= 12
                    monthly_rainfall = 0
                    if hour['rainfall'] == 'T':
                        continue
                    monthly_rainfall += float(hour['rainfall'])
            print(self.location_rainfall_list[location])

    def parse_time(self, time):         #接收來自self.data裡的time key

        time_format = '%Y-%m-%d %H:%M'  #定義時間格式
        try:
            dt = datetime.strptime(time, time_format)   #將接收到的time字串轉換成時間格式
            return dt
        except ValueError as e:                 #因為時間表示式0~23，但資料裡面有24，所以要寫例外處理
            time = time.replace('24:','23:')    #將時間字串中的24:取代成23:，不加:會將日期中的24取代成23
            dt = datetime.strptime(time, time_format)   #在將字串轉換成時間格式
            dt += timedelta(hours = 1)          #因為之前有將時間減1，故在這邊要將時間加回去
            return dt

    def plot_rainfall(self):                    #用來繪製報表圖例
        a_group = 12 
        #用來產生12個值得參數
        #index = [ 0  1  2  3  4  5  6  7  8  9 10 11]
        index = np.arange(a_group)

        bar_width = 0.35        
        opacity = 0.4

        plt.title('Rainfall per month')         #設定title文字
        plt.xlabel('month')                     #設定x軸標題
        plt.ylabel('Rainfall per month(mm)')    #設定y軸標題
        

        plt.xticks(index,('2015-09','10','11','12','2016-01','02','03','04','05','06','07','08'))   #設定X軸的各細項說明，第一組參數代表有幾組，第2個則是各組顯示的資訊
        plt.bar(left = index, height=tuple(self.location_rainfall_list['Taipei'])                   #開始畫長條，left是用來設定資料從哪邊開始畫，如果有複數個地點則代表有複數資訊
            , width =bar_width, align='center', color='g', label='Taipei', alpha=opacity)           #而height則是用各雨量統計數值來決定，故呼叫self.location_rainfall_list[各地點]，來放到tuple裡面
        plt.bar(left = index + bar_width, height=tuple(self.location_rainfall_list['Kaohsiung'])
            , width =bar_width, align='center', color='r', label='Kaohsiung', alpha=opacity)

        plt.legend()        #用來顯示長條副標(用bar裡面的color 以及 label來繪製)
        plt.show()          #顯示報表圖


def main():
    
    analyzer = WeatherAnalyzer()
    analyzer.load_json()
    analyzer.analyze_data()
    analyzer.plot_rainfall()

if __name__ == '__main__':
    main()