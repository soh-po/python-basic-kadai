array = ["水", "金", "地", "火", "木", "土", "天", "海", "冥"]
count = 0 # whileで使うカウントの初期化
length = len(array) # リストの要素数を取得

for i in array:
    print(i)

# ここまでfor文による表示、以下while文による表示

while count < length:
    print(array[count])
    count += 1
