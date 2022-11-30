animal = 'cat'

def f():
# 関数内からglobal変数を呼び出すことはできる
  # print(animal)
# 関数内で変数を宣言する前に呼び出すとerrorとなる
  animal= 'dog'
  print('local:', animal)
f()
print('global:', animal)

print('###########################################')
# 関数内からglobal変数を変数する方法
animal = 'cat'

def f():
  global animal
  animal = 'dog'
  print('local:', animal)
f()
print('global:', animal)

print('###########################################')


# locals(),globals()で宣言しているlocal変数,global変数が表示される
animal = 'cat'

def f():
  animal = 'dog'
  print('local:', locals())
f()
print('global:', globals())

print('###########################################')

animal = 'cat'

def f():
  """Test func doc"""
  print(f.__name__)
  print(f.__doc__)

f()
print('global:',__name__)