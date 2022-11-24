s = {1, 2, 3, 4, 5}
print(s)
# print(s[0])
# set型はindexのように[0]で取り出せない

# 要素を追加
s.add(6)
print(s)
# 集合型なので重複した追加はできない
s.add(6)
print(s)
# 要素を取り除く
s.remove(6)
print(s)

# 要素を全て取り除く
s.clear()
print(s)

