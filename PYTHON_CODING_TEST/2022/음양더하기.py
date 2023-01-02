def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


# 중요한 것 
signs [true, false, true]
이것은 문자열이 아니라 boolean일 뿐이다 !

그래서 if문으로 비교할 때도 if signs[i] == "true" 하면 안 된다.
if signs[i]: 로 하기 

# 다른 사람 풀이 

# zip을 활용해서 list 두 개를 동시에 돌릴 수 있다 ! 기억하기 
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer
