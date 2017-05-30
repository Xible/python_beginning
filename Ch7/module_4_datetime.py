'''
將datetime物件轉成字串來處理
'''

from datetime import datetime

def main():
    s1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(s1,type(s1))

    d1 = datetime.strptime("2017-5-29 17:02:29","%Y-%m-%d %H:%M:%S")
    print(d1,type(d1))


if __name__ == '__main__':
    main()