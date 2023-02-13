https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    dic ={}
    for term in terms:
        i, num = term.split(' ')
        dic[i]=num
    # {'A': '6', 'B': '12', 'C': '3'}
    
    y,m,d = map(int,today.split('.'))
    total = (y-2000)*12*28+m*28+d
    
    result = []
    for num in range(len(privacies)):
        p = privacies[num][:-2]
        p_y, p_m, p_d = map(int,p.split('.'))
        privacy_total = int(dic[privacies[num][-1]])*28 + (p_y-2000)*28*12+p_m*28+p_d
        print('total',total)
        print('privacy_total',privacy_total)
        if total >= privacy_total:
            result.append(num+1)
            
    return result