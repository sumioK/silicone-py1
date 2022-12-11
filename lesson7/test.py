import csv

with open('C:/Users/sumio/dev/python/silicone-py/lesson7/roboter.csv', 'r') as csv_file:
  reader = csv.DictReader(csv_file)
  for row in reader:
    print(row['Restaurant'], row['Count'])