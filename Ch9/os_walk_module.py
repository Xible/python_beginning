
'''
可以透過此方式找出想要的檔案，來做讀取或運用
'''
import os

def main():
    path = "C:\\Users\\xible.RAYARK\\Desktop\\python_beginning\\Ch9"
    for root, dirnames,filenames in os.walk(path):
        print("root = ",root)       #當前路徑
        print("dirnames" , dirnames)#當前路徑下的資料夾
        print("filenames",filenames)#當前資料夾底下的檔案，會用遞迴方式去尋找

        for file in filenames:
            if file.endswith(".py"):    #透過此函式搜尋結尾為.py的資料
                print("This is a Python file: ",file)
        print()


if __name__ == '__main__':
    main()