class Character:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print("私の名前は",self.name,"だ！")

class Brave(Character):
    def buy_weapon(self,weapon):
        self.weapon = weapon
        print(weapon,"を手に入れた")

class Wizard(Character):
    def introduce(self):
        print("私の名前は",self.name,"だ！")
        print(memory,"が使える魔法使いだ！\n")


    def learn_magic(self,magic):
        memory.append(magic)
        print(magic,"を覚えた！")
        print("現在使える魔法は",memory,"だ！\n")

naoki = Character("ナオキ")

kazuya = Brave("和也")
kazuya.buy_weapon("勇者の件")
kazuya.introduce()

memory = []

kei = Wizard("ケイ")
kei.introduce()
kei.learn_magic("回復魔法")
kei.introduce()
kei.learn_magic("攻撃魔法")
kei.introduce()

