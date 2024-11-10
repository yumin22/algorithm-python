n, b = input().split()
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0
for i, num in enumerate(n[::-1]):
    result += int(b)**i*num_list.index(num)

print(result)


# 파이썬의 int 함수는 임의의 진법 수를 10진법으로 변환하는데 사용할 수 있다(위 코드와 동일한 결과 도출)
# n, b = input().split()
# print(int(n, int(b)))