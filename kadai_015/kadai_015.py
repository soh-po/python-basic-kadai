class Human:
    # コンストラクタを定義
    def __init__(self, name, age):
        # 属性を定義
        self.name = name
        self.age = age

    # メソッドを定義
    def printinfo(self):
        print(self.name)
        print(self.age)

# インスタンス化
human = Human("侍太郎", 30)

human.printinfo()
