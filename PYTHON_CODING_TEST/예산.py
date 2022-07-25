# https://school.programmers.co.kr/learn/courses/30/lessons/12982

# 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.


# 해결방법
# 적은 수의 부서부터 지원해주기 (최대한 많은 수의 부서를 지원해줘야 하므로)

def solution(d, budget):
    ans = 0
    d.sort()
    for i in d:
        if budget-i>=0:
            budget-=i
            ans+=1
        else:
            break

    return ans