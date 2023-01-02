# https://school.programmers.co.kr/learn/courses/30/lessons/12921


# 첫번째로 푼 solution -> 효율성에서 시간초과 ㅠㅠ

def solution(n):
    cnt=0
    for x in range(1,n+1):
        if len([ x for i in range(1,x+1) if x%i==0 ])==2:
            cnt+=1
    return cnt

# 서칭을 해보니, 굳이 소수를 모든 수를 이용해서 나눌 필요 없고
# 자연수의 약수를 구할 때는 자기 자신의 제곱근까지만 확인해보면 된다는 것이다 !!

# 그래서 최종 작성한 코드

def solution(n):
    #     1 5 25 
# ex 26
    ans=0
    for x in range(2,n+1):
        cnt=0
        for i in range(2,int(x**(1/2))+1):
    #         소수가 아닐때
            if x%i==0:
                cnt+=1
                break
        if cnt==0:
            ans+=1
    return ans

# - for x in range에서 어차피 1은 의미가 없으므로 2부터 range 설정해주기
# - 소수 판별하기 위해 나눠줄 때 x의 제곱근 만큼만 for문 돌려주기 !! 
# - (중요) if x%i==0이 성립하면 소수가 아니므로 바로 break 해주기 

# 범위 내 존재하는 모든 소수 찾기 알고리즘(에라토스테네스의 체)를 이용해서도 소수를 구할 수 있다고 한다 !

# 에라토스테네스의 체 코드
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# 나중에 소수를 구하는 문제가 나왔을 때 외워서 풀어도 좋을 것 같다 ! (꿀팁)
