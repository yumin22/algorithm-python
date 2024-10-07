a_list =[]
b = 42

for i in range(10):
    a = int(input())
    a_list.append(a%42)
    result = set(a_list)
    a_list = list(result)

print(len(a_list))
