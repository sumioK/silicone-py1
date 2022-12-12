import csv
import os

# 挨拶、名前を聞く
print('=========================================================')
print('こんにちは!私はRobokoです。あなたの名前を教えてください')
print('=========================================================')
name = input('名前:')

# 名前を変数に代入し、好きなレストランを聞く
print('=========================================================')
print(f'{name}さん。どこのレストランが好きですか?')
print('=========================================================')

# レストランの名前を変数rに保存する
r = input('入力:')

# csvファイルを開き、中のデータを辞書restaurantsに代入
restaurants = {}

# roboter.csvが存在しない場合新たにファイルを作成する
if os.path.isfile('roboter.csv'):
  pass
else:
  with open('roboter.csv', 'w') as csv_file:
    fieldnames = ['Restaurant', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

# roboter.csvを開く
with open('roboter.csv', 'r+') as csv_file:
  reader = csv.DictReader(csv_file)

  #csvファイルの中身を辞書restaurantsに入れる 
  for row in reader:
    # restaurants.append({row['Restaurant']: row['Count']})
    restaurants[row['Restaurant']] = row['Count']
# もし既に存在しているレストランだったらCountを+1する
  if r in restaurants:
    row['Count'] += 1
# 存在していない場合、Countが１の状態で新しく作成する
  else:
    fieldnames = ['Restaurant', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Restaurant': r, 'Count': 1})

# 終了
print('=========================================================')
print(f'{name}さん、ご協力ありがとうございました。')
print('=========================================================')


