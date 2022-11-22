word = "python"
print(word[0])
print(word[1])
print(word[-1])

print(word[0:2])
print(word[:2])

print(word[2:6])
print(word[2:])

# 文字を置き換えるときは置き換えたい文字のみ指定しその他はスライスで上書きする
word = 'j' + word[1:]
print(word)

n = len(word)
print(n)

