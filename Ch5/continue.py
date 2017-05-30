'''
當i=5時，執行continue，回到for那行，
但是是從下一次得迴圈開始，而非重頭開始跑回圈
'''

def main():
    for i in range(10):
        if i == 5:
            continue  
        print("i = ",i)

if __name__ == '__main__':
    main()