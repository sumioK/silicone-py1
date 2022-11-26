is_empty = None
print(is_empty)

if is_empty is None:
  print('None!!')

if is_empty is not None:
  print('not None')

print('########################################')
print(1 == True)
# isは同じものでないと真にならない
print(1 is True)
print(True is True)
print(1 is not True)

