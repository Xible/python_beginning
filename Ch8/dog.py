'''
class 類別只是定義
'''

class Dog():
    def __init__(self,dog_type,height,weight,color):
        self.type = dog_type
        self.height = height
        self.weight = weight
        self.color = color

    def eat(self):
        print("eat something")

    def bark(self):
        print("bark~")

    def run(self):
        print("run...")

def main():
    dog = Dog("Chihuahua",40,30,"black") #將狗實例化出來，初始化出來

    dog.eat()
    dog.bark()
    dog.run()

    print(dog.weight)

    dog2 = Dog("Chihuahua",45,30,"white")
    dog.run()
    print(dog2.height)

if __name__ == '__main__':
    main()