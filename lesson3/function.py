def say_something():
  s = 'hi'
  return s

result = say_something()
print(result)



def what_is_this(color):
  if color == 'red':
    return 'tomato'
  else:
    return color

result2 = what_is_this('red')
print(result2)

def add_num(a: int, b: int) -> int:
  return a + b

r = add_num('a', 'b')
print(r)
