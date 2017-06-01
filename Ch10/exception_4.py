'''
自定義例外的類別，除了內建的例外類別外，也可以自己自定義類別
這時候要用到繼承
'''

def main():
    try:
        raise NameError("hello python")  
    except NameError:
        print("An exception occurs!")


if __name__ == '__main__':
        main()    