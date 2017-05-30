'''
import sys 模組，能夠根據使用者輸入的質不同，產生不同的結果 
(需再CMD輸入2個值)
'''
import sys

def main():
    print("Hello",sys.argv[0],sys.argv[1],sys.argv[2])
    

if __name__ == '__main__':
    main()