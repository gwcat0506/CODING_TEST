# 뭐가 틀린거죠

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
plus, minus, mul, div = map(int,input().split())


# 값 초기화 
minimum = 1e9
maximum = -1e9


def dfs(depth, total, plus, minus, mul, div):
    global minimum, maximum
    
    # return 조건
    # 숫자를 n개 만큼 모두 사용했을 때
    if depth == n:
        minimum = min(total, minimum)
        maximum = max(total, maximum)
        return 
    
    # print(total,minimum,maximum)
    if plus > 0:
        dfs(depth+1,total+nums[depth],plus-1, minus, mul, div)
        
        
    if minus > 0:
        dfs(depth+1,total-nums[depth],plus, minus-1, mul, div)
        
    if mul > 0:
        dfs(depth+1,total*nums[depth],plus, minus, mul-1, div)
        
    if div > 0:
        # 주의 !! 
        # int(total/nums[depth])를 꼭 써야됨
        dfs(depth+1,int(total/nums[depth]),plus, minus, mul, div-1)
        
    
# 처음에 깊이 1부터 탐색  
dfs(1,nums[0],plus, minus, mul, div)
print(maximum)
print(minimum)