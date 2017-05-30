'''
利用sys模組裡面的exit 函式來讓程式能夠在我們想要的地方中止
'''

import sys

def main():
    for i in range(5):
        if i == 3:
            sys.exit("i = " + str(i) + "exit")
        print("i = ",i)

if __name__ == '__main__':
    main()