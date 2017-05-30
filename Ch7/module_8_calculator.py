'''
import 自己做的模組 (.py檔)
要注意的是import的檔案必須跟此py在同個目錄下，這樣才抓到的
'''
import calculator as c # as name 可以用來簡化模組名稱，方便之後呼叫使用

def main():
    print(c.plus(1,2))
    print(c.minus(6,3))
    print(c.multiplied(3,4))
    print(c.divided(10,3))

if __name__ == '__main__':
    main()