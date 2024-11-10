n = int(input())
grade_list = list(map(int, input().split()))
m = max(grade_list)

for i in range(n):
    grade_list[i] = (grade_list[i]/m)*100

print(sum(grade_list)/n)