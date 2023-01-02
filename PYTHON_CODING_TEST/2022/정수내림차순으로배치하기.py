# https://school.programmers.co.kr/learn/courses/30/lessons/12933

#  n이 118372면 873211을 리턴하면 됩니다.

def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    return int(''.join(n))