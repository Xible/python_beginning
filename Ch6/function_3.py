
'''
**變數會將收到的參數變成一個dict字典{"Chinese",88........}，字典本身是無序的
所以不一定會按照你輸入參數的順序進行運算
'''
def sum(**scores):
    total = 0
    for subject, score in scores.items():
        print(subject,"is",score)
        total += score
    return total

def main():
    print("Total score = ",sum(Chinese=88,English=70,math=85,Science=95,Social=76))

if __name__ == '__main__':
    main()