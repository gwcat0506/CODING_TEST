# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    ans = 0
    while True:
        if ans==500:
            ans=-1
            break
        if num == 1:
            break
        if num%2==0:
            num = num/2
        else:
            num = num*3+1
        
        ans+=1
    return ans

# 다른 사람 풀이 
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1