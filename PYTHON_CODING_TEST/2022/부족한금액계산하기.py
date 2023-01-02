# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    
    answer = money-sum(price*i for i in range(1,count+1))

    return -answer if answer<0 else 0

# 리스트 컨프리헨션 연습하기 ㅎㅎ

# 다른 사람 풀이
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

# 음수일 때 0으로 대처한다면 max()를 이용해도 된다
# 아이디어 무엇..