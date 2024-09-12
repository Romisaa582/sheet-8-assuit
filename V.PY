n = int(input())

maybe = True

a, b = map(int, input().split())

if a != b:
    print("rated")
    exit()

previous = a

for _ in range(n - 1):
    a, b = map(int, input().split())
    
    if a != b:
        print("rated")
        exit()
    
    if a > previous:
        maybe = False
    
    previous = a

if maybe:
    print("maybe")
else:
    print("unrated")
