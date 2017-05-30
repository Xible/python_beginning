'''
pass 功能示範 
使此function先不做事，用來開發程式中，還沒實作功能時使用
'''
def main():
    score = 59
    if score >= 60:
        print("及格了")
    else:
        pass  #如果不打pass，會引發python縮排錯誤

if __name__ == '__main__':
    main()