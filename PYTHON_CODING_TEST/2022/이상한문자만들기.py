# https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    ans = []
    for word in s.split(" "):
        for j in range(len(word)):
            if j%2==0:
                ans.append(word[j].upper())
            else:
                ans.append(word[j].lower())
        ans.append(" ")
        
    return "".join(ans[:-1])
# 틀린코드.. 아직 이유는 모름.
def solution(s): 
    ans = ''
    for word in s.split(" "):
        for j in range(len(word)):
            if j%2==0:
                ans+=word[j].upper()
            else:
                ans+=word[j].lower()
        ans+=" "
                
    return ans.strip()

# 문자열 좌우 공백제거하기 -> a.strip()
# 대문자로 바꾸기 a.upper()
# 소문자로 바꾸기 a.lower()