n, k = map(int, input().split())

divisor = []
result = 0

for i in range(1, n+1):
    if (n % i == 0):
        divisor.append(i)
    
    
if k <= len(divisor):
    result = divisor[k-1] 

print(result)



