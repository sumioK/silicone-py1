def print_passage(func):
  def passage(*args, **kwargs):
    print('計算を開始します。')
    r = func(*args, **kwargs)
    print('計算が終了しました。結果を表示します。')
    return r
  return passage

@print_passage
def add_calc(a, b):
  return a + b
  
r = add_calc(10, 100)
print(r)
