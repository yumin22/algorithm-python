h, m = map(int, input().split())
# h가 시간, m이 분일 때... 입력한 시간 에서 -45분을 출력
# h*60 + m 에서 -45?
if m < 45:
    if h == 0:
        h = 23
        print(h, (m+15)) # m 단위가 60분인 걸 생각해서 60 - 45 = 15로 반대로 45보다 작다면 h - 1을 하고 m에는 15를 더해주는 전략
    else:
        print(h-1, m+15)
else:
    print(h, m-45)



