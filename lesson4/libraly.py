s = 'asdlktekjvdlsaijflekjfas;ldkjeikb'
# dにcがなかった場合に0を作成する(if文で分岐)
d = {}
for c in s:
  if c not in d:
    d[c] = 0
  d[c] += 1
print(d)

# setdefaultでcがない場合の数値を設定できる
d = {}
for c in s:
  d.setdefault(c, 0)
  d[c] += 1
print(d)



# collectionsのdefaultdictライブラリを使用
from collections import defaultdict

d = defaultdict(int)
for c in s:
  d[c] += 1
print(d)
