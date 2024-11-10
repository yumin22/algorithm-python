t =int(input())

quarter = 0
dime = 0
nickel = 0
penny = 0

for _ in range(t):
    c = int(input())
    quarter = c // 25
    c %= 25
    dime = c // 10
    c %= 10
    nickel = c // 5
    c %= 5
    penny = c 

    print(quarter, dime, nickel, penny, end=" ")