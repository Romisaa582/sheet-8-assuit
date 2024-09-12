n = int(input())

is_almost_lucky = False
for i in range(1, n+1):
    if all(digit in '47' for digit in str(i)) and n % i == 0:
        is_almost_lucky = True
        break

print("YES" if is_almost_lucky else "NO")