class Person(object):
  # 'クラスが作成されたときのみ実行されるため初期設定等を行う'
  def __init__(self, name):
    self.name = name

  def say_something(self):
    print('I am {}. hello'.format(self.name))
    self.run(5)

  def run(self, num):
    print('run' * num)


person = Person('Mike')
person.say_something()