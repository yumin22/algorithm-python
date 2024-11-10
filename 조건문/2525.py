a, b = map(int, input().split())
c = int(input()) # 60보다 큰 수가 들어올 수 있다는 걸 활용

a += c // 60
b += c % 60

if b >= 60: # >랑 >= 구분 잘 해서 써야된다!!!
    a += 1
    b -= 60

if a >= 24:
    a -= 24

print(a, b)
