import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))


# 0,1,2,3,4
for i in range(len(N_list)):
    # 4,3,2,1,0
    print(N_list[N-i-1])
    # 4,3,2,1
    for j in range(i-1):
        print(N_list[N-i-1],N_list[j-1])
        
            
            
    