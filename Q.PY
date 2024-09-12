name = input()
current = 'a'
moves = 0

for target in name:
    clockwise = abs(ord(target) - ord(current))
    counterclockwise = 26 - clockwise
    moves += min(clockwise, counterclockwise)
    current = target

print(moves)
