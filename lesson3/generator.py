l = ['Good morning', 'Good afternoon', 'Good night']

for i in l :
  print(i)

print('########################################')

def greeting():
  yield 'Good morning'
  yield 'Good afternoon'
  yield 'Good night'

for g in greeting():
  print(g)

print('####################################')
g = greeting()
# nextで一度処理から抜けるが、Good morningを出力したことは覚えている。
print(next(g))
print('@@@@@@@@@@@@@@')
print(next(g))
print('@@@@@@@@@@@@@@')
print(next(g))


print('#########################################')
def counter(num=10):
  for _ in range(num):
    # pythonはyieldを見るとgeneratorと判断する
    yield ' run'

c = counter()
g = greeting()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g)) 
