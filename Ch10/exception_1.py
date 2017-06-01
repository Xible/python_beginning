'''
try, except 語法

try:
    #可能發生例外的區塊
except:
    #例外發生時要做的區塊
else:
    #例外沒有發生時要做的事
finally:
    #不管有沒有發生例外都要做的事
'''

def main():
    try:
        n1 = 10
        n2 = 0
        print(n1 / n2)
    except ZeroDivisionError as e: #如果知道錯誤的類型，可以在except後面詳細定義
        print("Error: ",e)
    except:
        print("other error")



if __name__ == '__main__':
    main()