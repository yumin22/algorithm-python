m = int(input())
n = int(input())

decimal = []
for i in range(m, n+1):
    count = 0 
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count +=1
                break
        if count == 0:
            decimal.append(i)

if len(decimal)>0:
    print(sum(decimal))
    print(min(decimal))
else:
    print(-1)