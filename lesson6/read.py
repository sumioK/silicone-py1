s = """\
AAA
BBB
CCC
DDD
"""
# with open('test3.txt', 'w') as f:
#   f.write(s)
with open('test3.txt', 'r')as f:
  # print(f.read())
  while True:
    # chunkでチャンクごとに呼び出す
    chunk = 2
    # f.readlineで行ごとに読む
    line = f.readline(chunk)
    print(line)
    if not line:
      break