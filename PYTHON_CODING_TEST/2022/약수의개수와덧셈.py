# https://school.programmers.co.kr/learn/courses/30/lessons/77884



def solution(left, right):
    answer = 0
    
    for x in range(left,right+1):
        cnt=0
        for j in range(1,x+1):
            if x%j == 0:
                cnt+=1
                # print(j)
        if cnt%2==0:
            answer+=x
        else:
            answer-=x    
            
    return answer

# 다른 사람 풀이
# 제곱수는 약수가 홀수개인 것을 활용하였다.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


