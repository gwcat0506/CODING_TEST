# https://school.programmers.co.kr/learn/courses/30/lessons/12932


# 문자열을 거꾸로 부터 탐색한다. 

def solution(n):
    ans = []
    for i in str(n)[-1:-len(str(n))-1:-1]:
        ans.append(int(i))

    return ans

-1 0
-2 -1
...
-5 -4

# 로 가야해서 [-1:-len(str(n))-1:-1]: 짰다.

# 다른 사람 풀이 
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

# 이게 무슨.. 
