s = """\
AAA
BBB
CCC
DDD
"""

with open('test3.txt', 'r') as f:
  print(f.read())
  print(f.tell())
  print(f.read(1))
  f.seek(5)
  print(f.read(1))
