
n = int(input())

previous_magnet = input()
groups = 1
for _ in range(n - 1):
    current_magnet = input()
    
    if current_magnet != previous_magnet:
        groups += 1
    previous_magnet = current_magnet
print(groups)
