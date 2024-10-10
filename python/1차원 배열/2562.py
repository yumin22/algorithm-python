arr = []

for i in range(9):
    arr.append(int(input()))


max_number = max(arr)
print(max_number)
print(arr.index(max_number)+1)
