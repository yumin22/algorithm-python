n = int(input())
r = n
output = ""
for _ in range(n):
    output += "*"
    print(f'{output}'.rjust(r))