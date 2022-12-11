import csv

# 挨拶、名前を聞く
print('=========================================================')
print('こんにちは!私はRobokoです。あなたの名前を教えてください')
print('=========================================================')
name = input('名前:')

# 名前を変数に代入し、好きなレストランを聞く
print(f'{name}さん。どこのレストランが好きですか?')

# レストランの名前を変数rに保存する
r = input('入力:')

# csvファイルを開き、中のデータを辞書restaurantsに代入
restaurants = {}

with open('roboter.csv', 'r+') as csv_file:
  reader = csv.DictReader(csv_file)
  for row in reader:
    restaurants.append({row['Restaurant']: row['Count']})
# もし既に存在しているレストランだったらCountを+1する
  if restaurants[r]:
    row['Count'] += 1
# 存在していない場合、Countが１の状態で新しく作成する
  else:
    fieldnames = ['Restaurant', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Restaurant': r, 'Count': 1})

