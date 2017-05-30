'''
電腦需先pip install lxml、html5lib、pandas、beautifulsoup4、openpyxl才行
'''


import pandas 

def search():

    dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
    #透過pandas去讀取台銀匯率網站資料，在將資料放置dfs中
    currency = dfs[0] #將dfs list中的第一個元素放到currency中
    currency = currency.ix[:,0:5] #取出currency list中的前五個欄位資料
    currency.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']
    #將currency中的欄位重新命名，前面加 u 式改變其編碼為 unicode
    currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
    #將幣別欄位中的資料變成英文'原本顯示為美金(USD)美金(USD)'
    return currency


def main():
    
    search().to_excel('currency.xlsx') #將爬下來的資料存成xlsx檔


   
if __name__ == '__main__':
    main()