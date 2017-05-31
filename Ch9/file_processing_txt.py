'''
python 使用open()來開啟檔案，有下列2種語法
file = open("file path","mode")
(需搭配file.close()，不然無法將開啟之檔案關閉，之後可能會造成資料錯誤)
或是
with open("file path","mode") as file:
    #with body
(推薦使用此方法開啟檔案，檔案的操作只會在body裡面操作)
'''
'''
mode 模式分為r(讀取)、w(寫入)、a(寫入)、r+(讀取+寫入)、w+(寫入+讀取)、a+(寫入+讀取)
'''
import os

def main():
    '''
    txt example
    '''
    with open('test.txt','w') as file:  #使用w時，如果沒有該檔案則會新增一個新的
        file.write('Hello \n')          #使用\n來換行
        file.write('Pycone\n')

    with open('test.txt','w') as file:  #再次使用w會複寫既有檔案
        file.write('Hello \n')
        file.write('Pycones\n')

    with open('test.txt','a') as file:
        file.writelines(['Hello',' world\n','Pycone']) #writeline會將[]內的字串照順序寫入，效能上比用write好

    with open('test.txt','r') as file:
        content = file.read()
        print(content)
    '''    
    with open('test_example.txt','r') as file:   #讀取檔案時如果不存在該檔案，則會跳出錯誤
        content = file.readlines()
        print(content)

    with open('test_example.txt','r') as file:
        for line in file:
            print(line)
    ''' 

if __name__ == '__main__':
    main()