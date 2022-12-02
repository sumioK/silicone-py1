l = [1, 2, 3]
i = 5
# del l
# tryがない場合エラーが出る
try:
  l[0]
#exceptには条件も指定できる
except IndexError as ex:
  print('Don\'t worry: {}'.format(ex))
except NameError as ex:
  print(ex)
except Exception as ex:
  print('other:{}'.format(ex))
# tryが成功した場合のみ実行する
else:
  print('done')
  # finallyの処理は必ず最後に実行される(errorrが発生している場合も実行される)
finally:
  print('clean up')
