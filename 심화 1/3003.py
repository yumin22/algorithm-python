white = list(map(int, input().split()))
right_cnt = [1, 1, 2, 2, 2, 8]
for i in range(len(white)):
    if white[i] < 0:
        right_cnt[i] += white[i]
    else:
        right_cnt[i] -= white[i]

for j in right_cnt:
    print(j, end=" ") 
# 대괄호, 쉼표 없이 리스트 출력하는 방법
# join이나 다른 방법도 있긴 한데... 공부하자 !!
