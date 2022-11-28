# *argsを引数にすることで複数の引数をタプル化できる
def say_something(*args):
  print(args)

say_something('Hi', 'Mike', 'Nance')
print('###############################################')

# for文で回すことも可能
def say_greeting(*args):
  for arg in args:
    print(arg)

say_greeting('Hello', 'what\'s up')


print('###############################################')

# 自身でタプル化してアンパッキングすることも可能
def say_greeting(word, *args):
  print('word=', word)
  for arg in args:
    print(arg)
t = ('Hi', 'yeah')
say_greeting('Hello', *t)

