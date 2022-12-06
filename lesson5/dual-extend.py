class Person(object):
  def talk(self):
    print('talk')
  def run(self):
    print('person run')

class Car(object):
  def run(self):
    print('run')

# もし同じメソッドがあった場合先に読み込まれたメソッドが適用されるPerson→Car
class PersonCarRobbot(Person, Car):
  def fly(self):
    print('fly')


person_car_robot = PersonCarRobbot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()