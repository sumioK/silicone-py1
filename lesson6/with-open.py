# withステートメントを使用するとcloseしなくてもよい
with open('test2.txt', 'w') as f :
  f.write('Test\n')