
def main():
    number1 = 1
    number2 = 2

    try:                        #實務上常用來開啟檔案 
        if number1 < number2:  
            print(n)            #沒有定義n，故會執行except，不會執行else
    except Exception as e:
        print("excep: ",e)
    else:
        print("else except")
    finally:                    #一定會執行的部分，實務上大多用來關閉檔案
        print("finally")

    print("after exception")    #程式執行完[try, except]後並未終止，故會執行

if __name__ == '__main__':
    main()