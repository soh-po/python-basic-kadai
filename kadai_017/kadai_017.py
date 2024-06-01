class Human:
    # コンストラクタを定義
    def __init__(self, name, age):
        # 属性を定義
        self.name = name
        self.age = age

  
  # メソッドを定義
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は20歳以上（{self.age}歳）なので大人です。")
        else:
            print(f"{self.name}は20歳未満（{self.age}歳）なので大人ではありません。")


# インスタンスを複数作成してリストに追加する関数
def create_instances():
    human_info = []
    human_info.append(Human("大樹", 25))
    human_info.append(Human("健太", 18))
    human_info.append(Human("拓海", 30))
    human_info.append(Human("隼人", 22))
    human_info.append(Human("悠斗", 16))
    return human_info


# 関数の呼び出し
people_list = create_instances()

for people in people_list:
    people.check_adult()
