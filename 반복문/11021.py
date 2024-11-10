t = int(input())
case = 0

for _ in range(t):
    a, b = map(int, input().split())
    case +=1
    print(f"Case #{case}:", (a+b))