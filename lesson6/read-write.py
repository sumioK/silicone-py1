s = """\
AAA
BBB
CCC
DDD
"""

# with open('test3.txt', 'w+') as f:
#   f.write(s)
#   # writeのあとreadがしたい場合は、seekで先頭に戻る必要がある
#   f.seek(0)
#   print(f.read())


# w+で実行すると一度ファイルが空になる
# with open('test3.txt', 'w+') as f:
#   print(f.read())

# # r+では存在しないファイルは実行できない
# with open('test4.txt', 'r+')as f:
#   print(f.read())
#   f.seek(0)
#   f.write(s)