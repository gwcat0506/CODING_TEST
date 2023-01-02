# https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    wm="수박"
    ans = ''
    for i in range(n):
        if i%2==0:
            ans+=wm[0]
        else:
            ans+=wm[1]
    return ans


# 다른 사람 풀이 
def water_melon(n):
    s = "수박" * n
    return s[:n]