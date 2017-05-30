'''
Class example
We can do better 使用private method ( ex:__XXX )
盡量使用get以及set函式來修改值，可以避免很多不必要的失誤
'''

class Pikachu:
    def __init__(self,poke_name,poke_type,poke_weight,poke_height,poke_cp,poke_hp):
        self.name = poke_name
        self.__type = poke_type
        self.__weight = poke_weight
        self.__height = poke_height
        self.__cp = poke_cp
        self.__hp = poke_hp

    def get_name(self):    #透過get函式，讓使用者能夠拿到name的值
        return self.name

    def set_name(self,poke_name):
        self.__name = poke_name

    def get_hp(self):      #透過get函式，讓使用者能夠拿到__hp的值
        return self.__hp

    def set_hp(self,poke_hp):
        self.__hp = poke.hp

    def get_cp(self):      #透過get函式，讓使用者能夠拿到__cp的值
        return self.__cp

    def set_cp(self,poke_cp):
        self.__cp = poke_cp

    def first_skill(self):
        print('Thunder Shock')
        return 60

    def second_skill(self):
        print('Thunder')
        return 100

def main():
    pikachu = Pikachu('pika','Eletric',30,30,300,100)
    print('name = ',pikachu.name)
    #print(pikachu.__cp)  
    #這邊程式會報錯，說找不到該屬性。原因是pikachu.__cp是private，所以從外部會找不到該屬性
    print("cp = ",pikachu.get_cp())

    pikachu.name = 'chu'    #可以修改是因為name不是private屬性
    print("name = ",pikachu.name)

    pikachu.__cp = 1000     #這邊只是新增public 屬性的pikachu.__cp。而不是更改到private屬性的pikuchu.__cp的值
    print(pikachu.__cp)     
    print("cp = ",pikachu.get_cp())   #透過get_cp我們可以發現值還是原本的300

    pikachu.set_cp(400)     #透過set_cp function才能改變private屬性的值
    print('cp = ',pikachu.get_cp())


if __name__ == '__main__':
    main()