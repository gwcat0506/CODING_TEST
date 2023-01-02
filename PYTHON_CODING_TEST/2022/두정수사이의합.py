# https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    ans = 0
    for i in range(min(a,b),max(a,b)+1):
        ans+=i
    return ans



# 다른 사람의 풀이 
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))
