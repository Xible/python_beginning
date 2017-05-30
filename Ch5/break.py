'''
當i=5時，執行break，直接跳出該for迴圈
'''

def main():
    for i in range(10):
        if i == 5:
            break
        print("i = ",i)

if __name__ == '__main__':
    main()