d = {'x' : 10, 'y' : 20}
print(d.keys())
print(d.values())

# dictを上書き
d2 = {'x' :1000, 'j' : 500}
d.update(d2)
print(d)

# getは実行後もdictの内容は変わらない
print(d.get('x'))
print(d.get('z'))

# popは実行後にdictないからなくなる
print(d.pop('x'))
print(d)

# delは完全に削除
del d['y']
print(d)

del d

#clearはdictの中身のみを削除する 
d = {'x' :100, 'y' : 500}
d.clear()
print(d)

d = {'x' :100, 'y' : 500}
print('x' in d)
print('j' in d)

