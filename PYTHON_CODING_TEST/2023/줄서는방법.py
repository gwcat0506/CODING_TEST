# https://school.programmers.co.kr/learn/courses/30/lessons/12936

# 순열 모듈 import 
from itertools import permutations
 
def solution(n, k):

    a = [i for i in range(1,n+1)]
    per_list = list(permutations(a, n))
    
#     정렬하기
    per_list = sorted(per_list)
    return per_list[k-1]