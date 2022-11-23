def check() :
  print(len(seat))
  print(min <= len(seat) < max)

seat = []
min = 0
max = 5
check()

seat.append('p')
check()
seat.append('p')
check()
seat.append('p')
seat.append('p')
check()
seat.append('p')
check()
seat.pop(0)
check()