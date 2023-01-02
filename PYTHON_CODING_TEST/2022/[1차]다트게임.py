# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# 왜케 어렵냥 !!!!

def solution(dartResult):
    score=  []
    ten =''

    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            ten+=dartResult[i]
        elif dartResult[i]=='S':
            score.append(int(ten)**1)
            ten =''
        elif dartResult[i]=='D':
            score.append(int(ten)**2)
            ten =''
        elif dartResult[i]=='T':
            score.append(int(ten)**3)
            ten =''
            
        elif dartResult[i]=='*':
            if len(score)>1:
                score[-1]*=2
                score[-2]*=2
            else:
                score[-1]*=2
            
        elif dartResult[i]=='#':
            score[-1]*=-1
            
    return sum(score)

# 10을 어떻게 구별할지 모르고 있었는데.
dartResult = dartResult.replace('10','k')
point = ['10' if i == 'k' else i for i in dartResult]
print(point)
    
# 이런 식으로 문자열에서 10을 replace 해주고
# 그 수를 10으로 다시 나중에 바꿔주면된다.. ㄷ ㄷ
