class UppercaseError(Exception):
  pass


# 独自の例外処理を発生させる
def check():
  words = ['APPLE', 'orange', 'banana']
  for i in words:
    if i.isupper():
      raise UppercaseError(i)

try:
  check()
except UppercaseError as exc:
  print('This is my fault. Go next')
  
