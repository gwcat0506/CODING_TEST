# https://school.programmers.co.kr/learn/courses/30/lessons/12977


from itertools import combinations

def solution(nums):
    ans=0
    for l in list(combinations(nums,3)):
#         합계가 소수인지 확인
# 소수인지 확인 -> 수의 제곱근까지만 나눠서 확인해서 나눠지는 수가 없을경우 소수
        cnt=0
        for i in range(1,int((sum(l))**(1/2))+1):
            if sum(l)%i==0:
                cnt+=1
                # break
        if cnt==1:
            ans+=1
    return ans

# combinations 쓸 줄 알기 ! 
