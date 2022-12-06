class Person(object):
  
  kind = 'human'

  def __init__(self):
    self.x = 100

  # classmethodとすることで、オブジェクトを生成していない状態でもmethodを使用可能
  @classmethod
  def what_is_your_kind(cls):
    return cls.kind

  # class内の情報にアクセスするわけじゃないからクラスの外にあっても変わらない
  @staticmethod
  def about(year):
    print('about human {}'.format(year))

a = Person()
print(a.x)
print(a.what_is_your_kind())

# ()がないとクラスのオブジェクトになっていない
b = Person
# print(b.kind)
# print(b.x)
print(b.what_is_your_kind())
Person.about(1999)
