#a = int(input())
#b = input()
#print(a * int(b[2]))
#print(a * int(b[1]))
#print(a * int(b[0]))
#print(a * int(b))


# 내가 하려던 풀이 다시 !
a, b = map(str, input().split("\\n")) # 이렇게는 원래 안되는건가...? 그냥 input 을 두 번 받아야겠다ㅜ
print(int(a)*int(b[2]))
print(int(a)*int(b[1]))
print(int(a)*int(b[0]))
print(int(a)*int(b))