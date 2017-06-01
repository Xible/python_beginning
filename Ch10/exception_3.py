

def main():
    try:
        n1 = 10
        n2 = 0
        if n2 == 0:                                     
            raise ZeroDivisionError("Divided by zero~~.")     
            #透過raise 去觸發對應的例外exception
        print(n1 / n2)
    except ZeroDivisionError as e:             #再透過exception 去接收意外，並且讀取raise設定的文字
        print("ZeroDivisionError: ",e)

if __name__ == '__main__':
    main()