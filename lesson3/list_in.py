# リスト内包表記は処理が少ないため早く、メモリの使用も少なく済む

t = (1, 2, 3, 4, 5)


r = []
for i in t:
  r.append(i)

print(r)

print('###############################')

r = [i for i in t]
print(r)

print('###############################')




t = (1, 2, 3, 4, 5)

r = []
for i in t:
  if i % 2 == 0:
    r.append(i)

print(r)

print('###############################')

r = [i for i in t if i % 2 == 0]
print(r)

print('###############################')


t = (1, 2, 3, 4, 5)
t2 =  (5, 6, 7, 8, 9, 10)
r = []
for i in t:
  for j in t2:
    r.append(i * j)

print(r)

print('###############################')

# for文が二つ以上続く場合などは使わない方がよい
r = [i * j for i in t for j in t2]
print(r)