while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    if max((a, b, c)) >= sum((a, b, c)) - max((a, b, c)):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif (a == b and a != c) or (a == c and a!=b) or ( b == c and a!=b):
        print("Isosceles")
    else:
        print("Scalene")

        