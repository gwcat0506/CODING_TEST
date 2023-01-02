# https://school.programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    left_l = []
    right_l = []
    
    for x in sizes:
        if x[0] >= x[1]:
            left_l.append(x[0])
            right_l.append(x[1])
        else:
            left_l.append(x[1])
            right_l.append(x[0])
            
    return max(left_l)*max(right_l)

