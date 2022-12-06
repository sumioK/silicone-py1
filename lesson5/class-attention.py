class Car(object):
  def __init__(self, model=None):
    self.model = model

  def run(self):
    print('run')

class ToyotaCar(Car):
  def run(self):
    print('run fast')

class TeslaCar(Car):
  def __init__(self, model='Model S', 
              enable_auto_run=False,
              passwd='123'):
    super().__init__(model)
    self.__enable_auto_run = enable_auto_run
    self.password = passwd

  @property
  # 読み込み専用になる
  def enable_auto_run(self):
    return self._enable_auto_run
  
  @enable_auto_run.setter
  # 書き換え可能になる
  def enable_auto_run(self, is_enable):
    # 条件分岐でpasswdが一致するときのみ書き換え可能にする
    if self.password == '456':
      self._enable_auto_run = is_enable
    else:
      raise ValueError
  
  
  
  def run(self):
    print('run super fast')
    print(self.__enable_auto_run)
  def  auto_run(self):
    print('auto_run')  


tesla_car = TeslaCar('Model S', passwd='111')
tesla_car.run()
tesla_car.__enable_auto_run = 'xxxxxxx'
print(tesla_car.__enable_auto_run)

class T(object):
  pass

t = T()
t.name = 'Mike'
t.age = 20

print(t.name, t.age)