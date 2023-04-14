# https://school.programmers.co.kr/learn/courses/30/lessons/92335


def is_sosu(num):

    if num==1:
        return False 

    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False  
    return True
        
def make_jinsu(n,k):
    jinsu = ''
    
    while n:
        if n == 0:
            break
        jinsu += str(n%k)
        n = n//k
#         문자열 뒤집기, 최종 k진수 만들기 성공(jinsu)
    jinsu = jinsu[::-1]
    return jinsu

def solution(n, k):
    ans = 0
    jinsu = make_jinsu(n,k)
    
# 0으로 split한 리스트
    for i in jinsu.split('0'):
        if i != '':
#            빈칸이 아니면 소수인지 확인
            if is_sosu(int(i)):
                ans+=1
        # print(i)
          
    return ans

  
