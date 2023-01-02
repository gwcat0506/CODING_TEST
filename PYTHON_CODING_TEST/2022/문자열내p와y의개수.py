# https://school.programmers.co.kr/learn/courses/30/lessons/12916

# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True

def solution(s):
    ans = [0,0]
    # 중요 -> lower()하고 꼭 저장하기 ! 
    s=s.lower()
     
    for word in s :
        if word=='p':
            ans[0]+=1 
        elif word=='y':
            ans[1]+=1

    return True if ans[0]==ans[1] else False

# 다른 사람 풀이 
# 문자열에서 count를 통해 문자열을 셀 수 있다. 
def solution(s):
    return s.lower().count('p') == s.lower().count('y')