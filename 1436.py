n = int(input())

number = 666
cnt = 0

while True:
    if '666' in str(number):
        cnt +=1
    
    if cnt == n:
        break
    number += 1

print(number)