# 共通の友達など 演算できる
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)
print(my_friends - A_friends)

# list を集合に変換することで種類のみを表示する
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)

