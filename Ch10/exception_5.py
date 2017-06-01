
'''
except語法與 if elif一樣，如果上面已經有符合例外的情況發生，下面的例外就不會繼續檢查了
而在例外類別中，父類別會比子類別更容易通過檢查，所以要把父類別的檢查放比較後面
要注意的是如果觸發的例外之前有父類別的例外，則是會執行該父類別，而不是執行所觸發之例外
'''

def main():
    try:
        n1 = 10
        n2 = 0
        if n2 == 0:
            raise ZeroDivisionError("Divided by zero.")
        print(n1 / n2)

    except ArithmeticError as e:        #ArithmeticError 是 ZeroDivisionError的父類別
        print("ArithmetricError: ",e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError: ",e)
    except:                             #如果except後面不加類別，預設會是BaseException
        print("BaseException: ")

if __name__ == '__main__':
    main()