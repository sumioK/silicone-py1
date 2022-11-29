l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
  for word in words:
    print(func(word))

def sample_func(word):
  return word.capitalize()

# 引数に関数を入れている
change_words(l, sample_func)

print('##################################################')

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
  for word in words:
    print(func(word))
    
# lambdaを使用すれば１行で記載できる
sample_func = lambda word: word.capitalize()

change_words(l, sample_func)


print('##################################################')

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
  for word in words:
    print(func(word))
    
# 引数にlambdaを使用することができる
change_words(l, lambda word: word.capitalize())