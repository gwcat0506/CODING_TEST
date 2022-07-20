# 2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램


N = int(input())
n_list = []
for _ in range(N):
    str_N = input()
    n_list.append(str_N)

# Q1, Q2, Q3, Q4, AXIS
x_y = [0,0,0,0,0]
for i in n_list:
    A, B = i.split(" ")
    A = int(A)
    B = int(B)
    
    if A == 0 or B==0:
        x_y[4]+=1
    elif A > 0 :
        if B > 0:
            x_y[0]+=1
        else:
            x_y[3]+=1
    else:
        if B > 0:
            x_y[1]+=1
        else:
            x_y[2]+=1

print("Q1:",x_y[0])
print("Q2:",x_y[1])
print("Q3:",x_y[2])
print("Q4:",x_y[3])
print("AXIS:",x_y[4])