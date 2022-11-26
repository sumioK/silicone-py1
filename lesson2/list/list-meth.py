# 要素の場所を探す
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3,3))

# 要素の数を数える
print('#####################################')
print(r.count(3))

if 5 in r:
  print('exist')

# リストをソート(並べ替える)
print('#####################################')
r.sort()
print(r)

r.sort(reverse=True)
print(r)

r.reverse()
print(r)

# 文字列を引数で区切る
print('#####################################')
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

# リストをつなげる(''内の文字でつなげる)
x = ' '.join(to_split)
print(x)

