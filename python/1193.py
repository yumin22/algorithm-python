n = int(input())
line = 1

while n > line:
    n -= line
    line +=1

if ( line % 2 != 0): # 홀수 라인
    mole = line - n + 1
    demo = n
else: # 짝수 라인
    mole = n
    demo = line - n + 1

print(f'{mole}/{demo}')
