t = int(input())

n = 0
for _ in range(t):
    a, b = map(int, input().split())
    n += 1
    print(f"Case #{n}: {a} + {b} = {a+b}")
