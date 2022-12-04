# import を,で区切って横並びにするのは勧められていない
import collections, sys

# 一つずつアルファベット順に並べる(ジャンルごとに一行開ける)
# 初めに組み込み
import collections
import os
import sys

# 次に３rｄpartyのライブラリ
import termcolor

# 次に自分の作ったライブラリ
import lesson_package

# ローカルファイル
import config



print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
