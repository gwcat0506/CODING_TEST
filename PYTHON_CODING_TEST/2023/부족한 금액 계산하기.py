# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    ans=0
    for i in range(1,count+1):
        ans+= i*price
    
    return 0 if money-ans>=0 else abs(money-ans)
    