t = (1, 2, 3, 4, 1, 2)
print(t)
# t[0] = 100 タプルは要素の書き換えに対応していない

print(t[0])
print(t[-1])
print(t.index(1))
print(t.index(1, 1))
t.count(1)

# tapleは読み取り専用として使うことが多い

t = ([1, 2, 3], [4, 5, 6])
print(t)
# taple内にlistをネストしているとlistの内容は書き換え可能
t[0][0] = 100
print(t)

# tappleはパレンティスがなくてもカンマがあるとtapleになる
t = 1, 2, 3
print(type(t))
print(t)

t = ()
print(t)
print(type(t))

# カンマを付けるとタプルになってしまうため注意
# t = 1,
# print(t + 100)

new_taple = (1,)+(2, 3, 4)
print(new_taple)
