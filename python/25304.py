x = int(input())
y = int(input())

# sum 변수에 할당해주기
sum = 0
for _ in range(y):
    a, b = map(int, input().split())
    sum += (a*b)

if sum == x:
    print("Yes")
else:
    print("No")