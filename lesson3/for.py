some_list = [1, 2, 3, 4, 5]

i = 0
while i <len(some_list):
  print(some_list[i])
  i += 1

print('#########################################')
for i in some_list:
  print(i)

print('#########################################')
for s in 'abcde':
  print(s)

print('#########################################')
for word in ['my', 'name', 'is', 's']:
  print(word)


print('#########################################')
for word in ['my', 'name', 'is', 's']:
  if word == 'name':
    break
  print(word)

print('#########################################')
for word in ['my', 'name', 'is', 's']:
  if word == 'name':
    continue
  print(word)
