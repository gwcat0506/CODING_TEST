# https://www.acmicpc.net/problem/10815


N = int(input())
N_list = set(list(map(int, input().split())))

M = int(input())
M_list = list(map(int, input().split()))

# print(N_list)
# print(M_list)

for i in M_list:
    if i in N_list:
        print(1, end = " ")
    else:
        print(0, end = " ")
        
        
        
# 옛날 풀이 sys 이용

import sys

#집합이용하기
input() # 필요없음
n = set(map(int,sys.stdin.readline().split())) #입력받은 숫자들 집합 지정
input() # 필요없음
m = list(map(int,sys.stdin.readline().split()))

for i in m:
    if i in n: 
        print(1, end=' ')#end 통해서 줄바꿈 X

    else:
        print(0, end=' ')