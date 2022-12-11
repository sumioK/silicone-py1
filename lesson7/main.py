import csv

restaurants = {}

# 挨拶、名前を聞く
print('=========================================================')
print('こんにちは!私はRobokoです。あなたの名前を教えてください')
print('=========================================================')
name = input('名前:')

# 名前を変数に代入し、好きなレストランを聞く
print(f'{name}さん。どこのレストランが好きですか?')

# レストランの名前を変数に保存する
r = input('入力:')
restaurants.append(r)
print(restaurants)

# レストランの名前と回数をcsvファイルへ出力する
with open('roboter.csv', 'w', newline='', encoding='utf-8') as csv_file:
  fieldnames = ['Restaurant', 'Count']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'Restaurant': r, 'Count': 1})
  

with open('roboter.csv', 'r') as csv_file:
  reader = csv.DictReader(csv_file)
  for row in reader:
    restaurants.append({row['Restaurant']: row['Count']})
