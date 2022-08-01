# https://school.programmers.co.kr/learn/courses/30/lessons/68935


def solution(n):
    zin = []
    ans = 0 
    while True:
        if n//3==0:
            zin.append(n)
            break
        else:
            zin.append(n%3)
            n = n//3
#     list 순서 뒤집기
    # zin = reversed(zin)
    for i in range(len(zin)):
        ans= ans+zin[i]*(3**(len(zin)-i-1))
    
    return ans


#  다른 사람 풀이 

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

# int(숫자(스트링가능),진법) 을 사용하면 쉽게 몇진법으로 바꿀 수 있다 

