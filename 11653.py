n = int(input())
result = []
count = 2

while (n != 1):
    if n % count == 0:
        result.append(count)
        n = n / count
    else:
        count +=1

for i in result:    
    print(i)


