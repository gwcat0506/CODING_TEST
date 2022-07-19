
num = int(input())

A = num//300

B = (num-300*A)//60

C = (num-300*A-60*B)//10

if (num-300*A-60*B)%10!=0:
    print(-1)
else:
    print(A,B,C)