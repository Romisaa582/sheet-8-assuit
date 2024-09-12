
n = int(input().strip())
cards = list(map(int, input().strip().split()))
sereja_points = 0
dima_points = 0
left = 0
right = n - 1
turn = 0


while left <= right:
    if cards[left] > cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1
    
    if turn == 0:
        sereja_points += chosen_card
        turn = 1
    else:
        dima_points += chosen_card
        turn = 0
print(sereja_points, dima_points)
