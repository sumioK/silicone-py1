for fruit in ['apple', 'banana', 'orange']:
  print(fruit)
else:
  print('I ate all!')


print("###############################################")
for fruit in ['apple', 'banana', 'orange']:
  if fruit == 'banana':
    break
  print(fruit)
else:
  print('I ate all!')

print("###############################################")
for fruit in ['apple', 'banana', 'orange']:
  if fruit == 'banana':
    continue
  print(fruit)
else:
  print('I ate all!')