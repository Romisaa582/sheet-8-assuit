for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print("not prime")
        continue

    f1, f2 = 0, 1
    for i in range(2, n+1):
        f1, f2 = f2, f1 + f2

    is_prime = True
    for i in range(2, int(f2**0.5) + 1):
        if f2 % i == 0:
            is_prime = False
            break

    print("prime" if is_prime else "not prime")