a, b, c = map(int, input().split())

circum = sum((a, b, c))

if max((a, b, c)) >= sum((a, b, c)) - max((a, b, c)):
    circum = (sum((a, b, c))-max((a, b, c)))*2 -1  
    print(circum)
else:
    print(circum)

