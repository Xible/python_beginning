'''
下列為2種函數，一種為常見的，一種為自己呼叫自己，稱為recursion 遞迴呼叫
要注意的是，如果不是非必要的話(確認傳入參數不會太多、用非遞迴寫法來實作太過複雜)
建議還是使用非遞迴的寫法會比較好，不然可能會導致stack overflow
'''

def factorial(n):  #非遞迴寫法
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def factorials(m):  #遞迴寫法
    if m > 1:
        return m * factorials(m - 1)
    else:
        return 1

def main():
    print(factorial(3))
    print(factorials(4))

if __name__ == '__main__':
    main()