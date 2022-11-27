d = {'x' : 100, 'y': 200}
for v in d :
  print(v)

print('################################')
for k, v in d.items():
  print(k, ':', v)
  
print('#################################')
# d.items()は集合で処理される
print(d.items())
