# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    
    return s[len(s)//2-1]+s[len(s)//2] if len(s)%2==0 else s[len(s)//2]

# 다른 사람 풀이 
str[(len(str)-1)//2:len(str)//2+1]