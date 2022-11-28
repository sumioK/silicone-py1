def menu(entree='beef', drink='wine'):
  print(entree, drink)

menu(entree='beef', drink= 'coffee')
print('###############################################')

# **kwargsを使用するとディクショナリーの形で出力される
def menu(**kwargs):
  print(kwargs)

menu(entree='beef', drink='wine')

print('################################################')

def menu(**kwargs):
  for k, v in kwargs.items():
    print(k,v)

menu(entree='beef', drink='wine')

# ディクショナリーを用意するパターン
def menu(**kwargs):
  for k, v in kwargs.items():
    print(k, v)

d = {
  'entree': 'beef',
  'drink': 'ice coffe',
  'dessert': 'ice'
}
menu(**d)

# タプル化、ディクショナリー化を同時に行う
print('###############################################')
def menu(food, *args, **kwargs):
  print(food)
  print(args)
  print(kwargs)

menu('apple', 'banana', 'cocoa', dessert='ice')
