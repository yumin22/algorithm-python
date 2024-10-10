n, m = map(int, input().split())

box = [i for i in range(1, n + 1)]

temp = 0

for _ in range(m):
    i, j = map(int, input().split())
    temp = box[i - 1]
    box[i - 1] = box[j - 1]
    box[j - 1] = temp

for i in range(n):
    print(box[i], end=" ")
