# https://school.programmers.co.kr/learn/courses/30/lessons/12926

# 알파벳 밀기 
# 꿀팁 -> 프로그래머스 출력으로 ord() 출력하면서 해당 문자열의 아스키코드 구하기 
def solution(s, n):
    ans=''
    for i in range(len(s)):
        if s[i]==" ":
            ans+=" "
#         대문자일때
        elif ord(s[i])>=65 and ord(s[i])<=90:
            if ord(s[i])+n>90:
                ans+=chr(ord(s[i])+n-26)
            else:
                ans+=chr(ord(s[i])+n)
#         소문자일때
        elif ord(s[i])>=97 and ord(s[i])<=122:
            if ord(s[i])+n>122:
                ans+=chr(ord(s[i])+n-26)
            else:
                ans+=chr(ord(s[i])+n)
    
    return ans
# K = 75

# "A" = 65
# "Z" = 90


# a 97
# z 122