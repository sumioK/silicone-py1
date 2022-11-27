def menu(entree, drink, dessert):
  print(entree)
  print(drink)
  print(dessert)

# 順番または引数が正しくないといけない
menu(entree='beef', drink='beer', dessert='dessert')


print('########################################################')
def menu(entree='beef', drink='whine' ,dessert='ice'):
  print(entree)
  print(drink)
  print(dessert)

menu(entree = 'checken')


print('########################################################')
def test_func(x, l=[]):
  l.append(x)
  return l

y = [1, 2, 3]
r = test_func(100, y)
print(y)

# 100を2回渡されると100が2買い渡されてしまう。
# default引数で関数を使用すべきではない
r = test_func(100)
print(r)
r = test_func(100)
print(r)


print('########################################################')
def test_func(x, l =None):
  # 関数の中で空のリストを渡せば解決できる
  if l is None:
    l = []
  l.append(x)
  return l

r = test_func(100)
print(r)
r = test_func(100)
print(r)
