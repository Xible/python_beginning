'''
json格式為key:value的關係
ex:
{
    key1:value1
    key2:[value2,value3....]
    key3:{
        key4:value4
    
    }
}
'''

import json

'''
json example
'''

def main():
    with open('player.json') as file:   #開啟json檔案，沒有給mode的話，預設是read模式
        player = json.load(file)        #將json檔存入player中
        print(player)                   #dict型態，故不一定會按照json中的順序傳入
        print(type(player))
        print("Player's name = ",player["name"])  #取player中 "name" key的value

    with open('warriors_player.json','w') as file:  #創建一個json檔
        player = {}
        player["name"] = "Curry"
        player["age"] = 28
        player["championship"] = [2014]
        json.dump(player, file, indent = 4)
        #利用json.dump函式放上我們要存的資料以及要輸出的檔案，indent意思為要縮排幾個空格


if __name__ == '__main__':
    main()