

N = int(input())
a_list = list(map(str,input().split()))
print(a_list)
x_y= [1,1]
for i in range(len(a_list)):
    if a_list[i] == 'L':
        if x_y[1]-1 >= 1 : 
            x_y[1]-=1
    if a_list[i] == 'R':
        if x_y[1]+1 <= N: 
            x_y[1]+=1
    if a_list[i] == 'U':
        if x_y[0]-1 >= 1: 
            x_y[0]-=1
    if a_list[i] == 'D':       
        if x_y[0]+1 <= N: 
            x_y[0]+=1

print(x_y[0],x_y[1])