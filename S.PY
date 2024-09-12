n, k = map(int, input().split())
count = 0

for i in range(n):
    a = int(input())
    digits = set(str(a))
    if len(digits) == k + 1 and all(int(d) in digits for d in range(k + 1)):
        count += 1

print(count)

