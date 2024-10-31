words = [input() for _ in range(5)]

for j in range(15): # 그럼 만약 15보다 크면??
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end="")

