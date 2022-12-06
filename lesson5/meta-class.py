import abc
class Person(metaclass=abc.ABCMeta):
  def __init__(self, age=1):
    self.age = age
  # 必ず実装しなければならないメソッドを定義する
  @abc.abstractmethod
  def drive(self):
    pass

class Baby(Person):
  def __init__(self, age = 1):
    if age < 18:
      super().__init__(age)
    else:
      raise ValueError
  def drive(self):
    raise Exception('you can not')

class Adult(Person):
  def __init__(self, age = 18):
    if age >= 18:
      super().__init__(age)
    else:
      raise ValueError
  def drive(self):
    print('ok')


baby = Baby()
adult = Adult()
adult.drive()

class Car(object):
  def __init__(self, model=None):
    self.model = model

  def run(self):
    print('run')

  def ride(self, person):
    person.drive()

# car = Car()
# car.ride(adult) 