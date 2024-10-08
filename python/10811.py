n, m = map(int, input().split())


n_list=[i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    reverse_list = n_list[i-1:j]
    reverse_list.reverse()
    n_list[i-1:j] = reverse_list

for i in range(n):
    print(n_list[i], end=" ")


