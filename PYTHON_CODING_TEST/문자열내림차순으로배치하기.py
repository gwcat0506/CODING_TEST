# https://school.programmers.co.kr/learn/courses/30/lessons/12917


def solution(s):
    l = [ord(i) for i in s ]
    l.sort(reverse=True)
    ans =""
    for i in l :
        ans+=chr(i) 
    return ans

print(solution("Zbcdefg"))


# 다른 사람 풀이..
def solution(s):
    return ''.join(sorted(s, reverse=True))

# 이렇게 간단한 문제라니..
# "".join으로 문자열 붙여주기 !! 