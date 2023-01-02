def solution(numbers):
    set_num = set([0,1,2,3,4,5,6,7,8,9])
    answer = set_num-set(numbers)
    return sum(answer)


# 다른 사람들의 풀이
def solution(numbers):
    return 45 - sum(numbers)


# 이렇게 간단하게 생각하다니.. 대단 !! 