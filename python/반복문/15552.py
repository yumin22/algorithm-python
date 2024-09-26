import sys

# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
# input() 대신 사용하는 방식 sys.stdin.readline()
# 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)