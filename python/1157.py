n = input().upper()
n_list = list(set(n))
max_cnt = 0
max_word = ''
for i in n_list:
    if max_cnt > n.count(i):
        continue
    elif max_cnt == n.count(i):
        max_word = '?'
    else:
        max_cnt = n.count(i)
        max_word = i
print(max_word)