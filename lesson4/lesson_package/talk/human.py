# from .. import utils 相対パスを使用することはあまり勧められない
from lesson_package import utils 

def sing():
  return 'sing'

def cry():
  return utils.say_twice('cry')