num_tuple = (10, 20)
print(num_tuple)

# tupleの展開
x, y = num_tuple
print(x)
print(y)

min, max = 0, 100
print(min, max)

i = 10
j = 20
print('i =',i)
print('j =', j)

# iとjを入れ替える
tmp = i
i = j
j = tmp

print('i =', i)
print('j =', j)

# unpackingを使うと1行で入れ替え可能
a = 100
b = 200
print('a =', a)
print('b =', b)
a, b = b, a
print('a =', a)
print('b =', b)