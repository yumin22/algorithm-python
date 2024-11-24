x, y = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
result_x = 0
result_y = 0

if x == x2:
    result_x = x3
elif x == x3:
    result_x = x2
else: 
    result_x = x

if y == y2:
    result_y = y3
elif y == y3:
    result_y = y2
else: 
    result_y = y

print(result_x, result_y, end=" ")

