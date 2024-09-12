def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

n, m = map(int, input().split())

next_prime = n + 1
while not is_prime(next_prime):
    next_prime += 1

if next_prime == m:
    print("YES")
else:
    print("NO")
