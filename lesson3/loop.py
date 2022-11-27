# count = 0
# while count < 5:
#   print(count)
#   count += 1

count = 0
while True:
  if count >= 5:
    # breakは完全にループが終了する
    break

  if count == 2:
    count += 1
    # continue は終了するのではなくスキップする
    continue


  print(count)
  count += 1