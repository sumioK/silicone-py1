class Person(object):
# コンストラクタ
  def __init__(self, name):
    self.name = name

  def say_something(self):
    print('I am {}. hello'.format(self.name))
    self.run(5)

  def run(self, num):
    print('run' * num)
# デストラクタ
  def __del__(self):
    print('goodbye'    )

person = Person('Mike')
person.say_something()
print('######################################')