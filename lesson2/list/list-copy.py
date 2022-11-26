i = [1, 2, 3, 4, 5]
j = i
# jに100を代入するとiの0番目も100になってしまう
j[0] = 100

print('j =', j)
print('i =', i)

# copyメソッドを使うことで避けられる
x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

print('#####################################################')
x = 20
y = x
y = 5
print(id(x))
print(id(y))
print(y)
print(x)

# listを使うとidが同じになる
x = [ 'a', 'b']
y = x
y[0] = 'p'
print(id(y))
print(id(x))
print(y)
print(x)