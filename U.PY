n = int(input())

if n >= 0:
    print(n)
else:
    n1 = int(str(n)[:-1])
    n2 = int(str(n)[:-2] + str(n)[-1])
    print(max(n1, n2))
