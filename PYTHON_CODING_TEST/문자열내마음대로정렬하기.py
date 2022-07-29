# https://school.programmers.co.kr/learn/courses/30/lessons/12915


def solution(strings, n):
    
    return sorted(strings, key= lambda x:(x[n],x))

# [꿀팁]
# sorted(strings, lambda x: (기준1, 기준2)) 를 통해 기준 적용 우선순위가 가능하다