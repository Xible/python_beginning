'''
csv 格式
header1,header2,header3,...,herdern
value1_1,value1_2,value1_3,....value1_n
...
value
'''

import csv

def main():
    with open('TSMC.csv','r') as file:
        for row in csv.reader(file):
            print(row)

if __name__ == '__main__':
    main()