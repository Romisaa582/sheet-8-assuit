
n, x = map(int, input().split())


distressed_kids = 0


for _ in range(n):
    op, di = input().split()
    di = int(di)
    
    if op == '+':
        
        x += di
    elif op == '-':
        
        if x >= di:
            x -= di
        else:
            distressed_kids += 1


print(x, distressed_kids)
