# from lesson_package import utils # as で名前を指定できる
# from lesson_package.talk import *
# r = utils.say_twice('hello')
# print(r)

# print(human.sing())
# print(human.cry())


# print(animal.sing())
# print(animal.cry())
try:
  from lesson_package import utils
except ImportError:
  from lesson_package.tools import utils

utils.say_twice('word')
