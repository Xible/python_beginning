'''
以下介紹常用模組 datetime
'''


from datetime import datetime

def main():
    d1 = datetime.now()
    print(d1)
    print(d1.date())

    d2 = datetime(2017,5,30)
    print(d2)

    delta = d2- d1
    print(delta)
    print(delta.days)
    print(delta.seconds)


if __name__ == '__main__':
    main()