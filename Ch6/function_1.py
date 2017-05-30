'''
參數傳入時可以不用按照func的變數順序，
可以利用變數=XX的方式來給予func參數
'''
def student(name,age,score):
    print(name,"is",age,"years old",score,"scores")

def main():
    student("David",18,90)
    student(age=20,score=100,name="John")


if __name__ == '__main__':
    main()