croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()

for i in croatia:
    n = n.replace(i, "*")
print(len(n))