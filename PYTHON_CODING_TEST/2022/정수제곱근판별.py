# https://school.programmers.co.kr/learn/courses/30/lessons/12934

# 해당 수가 제곱근인지 아닌지
def solution(n):
    
    if int(n**(1/2))**2 == n:
        return (n**(1/2)+1)**2
    return -1