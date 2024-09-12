
x1, x2, x3 = map(int, input().split())
coords = sorted([x1, x2, x3])
median = coords[1]
total_distance = abs(coords[0] - median) + abs(coords[1] - median) + abs(coords[2] - median)
print(total_distance)