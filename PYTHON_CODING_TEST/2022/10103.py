
N = int(input())

A = 100
B = 100

for i in range(N):
    str_N = input()
    x, y = str_N.split(" ")
    x = int(x)
    y = int(y)
    
    if x>y:
        B-=x
    elif x<y:
        A-=y
    else:
        pass
    
print(A)
print(B)