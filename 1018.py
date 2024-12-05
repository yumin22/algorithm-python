n, m = map(int, input().split())
n_list = []

for _ in range(n):
    n_list.append(input())


result = []
for i in range(n-7):
    for j in range(m -7):
        is_B = 0
        is_W = 0

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2==0:
                    if n_list[k][l] != 'B':
                        is_B +=1
                    if n_list[k][l] != 'W':
                        is_W +=1
                else:
                    if n_list[k][l] != 'W':
                        is_B +=1
                    if n_list[k][l] != 'B':
                        is_W +=1
        result.append(is_B)
        result.append(is_W)

print(min(result))                
