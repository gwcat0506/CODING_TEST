# https://school.programmers.co.kr/learn/courses/30/lessons/42628



def solution(operations):
    ans = []
    for oper in operations:
        print(ans)
        if oper[0]=='I':
            ans.append(int(oper[2:]))
            print(ans)
        if oper=='D 1':
            if len(ans)>=1:
                del ans[ans.index(max(ans))] 
        if oper=='D -1':
            if len(ans)>=1:
                del ans[ans.index(min(ans))] 
    if len(ans)<=0:
        return [0,0]
    else:
        return [max(ans),min(ans)]
        
    return answer