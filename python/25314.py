n = int(input())
answer = "int"

for _ in range(n//4): # 몫 연산자
    answer = "long " + answer

print(answer)


