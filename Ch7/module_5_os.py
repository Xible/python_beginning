'''
import os 模組，可以獲得系統的資訊
'''
import os

def main():
    print(os.getcwd())  #取得當前資料夾所在位置
    print(os.listdir()) #列出該資料夾底下有哪些檔案
    os.mkdir("test")    #新增資料夾"test"
    print(os.listdir())
    os.rmdir("test")    #移除資料夾"test"
    print(os.listdir())

if __name__ == '__main__':
    main()