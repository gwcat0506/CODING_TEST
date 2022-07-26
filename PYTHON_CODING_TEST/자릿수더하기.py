# https://school.programmers.co.kr/learn/courses/30/lessons/12931


def solution(n):
    ans=0
    for i in str(n):
        ans+=int(i)
    return ans



# 다른 사람 풀이 
def sum_digit(number):
    return sum([int(i) for i in str(number)])