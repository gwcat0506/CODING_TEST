# 실패 후 참고해서 해결 -> https://recordofwonseok.tistory.com/378
# 연속되는 수의 합이 아니라 그냥 부분집합의 합이다 !

import sys
from itertools import combinations

input = sys.stdin.readline

n,s = list(map(int,input().split()))
nums = sorted(list(map(int,input().split())))

ans = 0
for i in range(1,n+1):
    combis = list(combinations(nums,i))
    for combi in combis:
        if sum(combi)==s:
            ans+=1
            
print(ans)
