y = [1, 2, 3]
x = 1

if x in y:
  print('in')

if 100 not in y:
  print('not in')

a = 1
b = 2

# not ==はあまり好まれない
if not a == b:
  print('Not equal')

if a != b:
  print('Not equal')

print('#############################################')

is_ok = True
if is_ok:
  print('hello')

# notは以下のような場合に使う

if not is_ok:
  print('hello')