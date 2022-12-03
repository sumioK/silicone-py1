from lesson_package import utils # as で名前を指定できる
from lesson_package.talk import human
r = utils.say_twice('hello')
print(r)

print(human.sing())
print(human.cry())
