# https://school.programmers.co.kr/learn/courses/30/lessons/70128


# 리스트 두 개를 zip을 이용해서 한번에 for문을 돌렸다.
def solution(a, b):
    answer = 0
    
    for i, j in zip(a,b):
        answer+=i*j
    
    return answer


# 다른 사람 풀이
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

# 이런 생각을 할 수 있다니..
# 리스트 컴프리헨션 활용할 수 있도록 노력하기! 