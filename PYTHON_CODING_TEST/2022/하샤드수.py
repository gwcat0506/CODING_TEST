# https://school.programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    a = list(str(x))
    ans=0
    for i in a:
        ans+=int(i)
    
    return True if x%ans==0 else False
