'''
利用*變數的方式，可以接受不定數量的參數，來完成運算
'''

def sum(*num):
    total = 0
    for n in num:
        total += n
    return total

def main():
    print("sum = ",sum(1,2,3,4,5))

if __name__ == '__main__':
    main()