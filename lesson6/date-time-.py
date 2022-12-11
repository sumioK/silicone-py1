import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%F'))

print('##########################################################')
today = datetime.date.today()
print(today)
print(today.strftime('%d/%m/%y'))

print('##########################################################')
t = datetime.time(hour=1, minute= 10, second= 5, microsecond=100)
print(t)
print(t.strftime('%H_%M_%S_%f'))

print('##########################################################')
# まえの日時を表示する
print(now)
d = datetime.timedelta(weeks=-1)
print(now + d)



import time
print('#')
time.sleep(1)
print('##')
print(time.time())

import os
import shutil

file_name = 'test.txt'
if os.path.exists(file_name):
  shutil.coppy(file_name, "{}.{}".format(
    file_name, now.strftime('%Y_%m_%d_%H_%M_%S_%F')))

with open(file_name, 'w')as f:
  f.write('test')