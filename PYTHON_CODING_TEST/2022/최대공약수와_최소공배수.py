# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = [0,0]
    for i in range(1,n*m+1):
        if n%i==0 and m%i==0:
            answer[0] = i
        if i%n==0 and i%m==0:
            answer[1] = i
            break
            
        
    return answer


