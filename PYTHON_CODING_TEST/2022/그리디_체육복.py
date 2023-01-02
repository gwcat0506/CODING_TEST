# https://school.programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    answer = n-len(lost)
    
    
    for i in range(len(lost)):
        if lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            answer+=1
        elif lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            answer+=1
    
    
    return answer