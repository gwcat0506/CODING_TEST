# https://school.programmers.co.kr/learn/courses/30/lessons/1845



# 처음에는 combination 생성해서 풀었으나 -> 문제를 잘 읽어보니 그럴 필요가 없었다.
from itertools import combinations

def solution(nums):
    ans = 0
    
    if len(set(nums)) > len(nums)//2:

        len(nums)//2
            
    else:
        return len(set(nums))
                
    return ans

# 다시 줄여서 풀기
def solution(nums):
    
    return len(nums)//2 if len(set(nums)) > len(nums)//2 else len(set(nums))

