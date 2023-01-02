
def ox_print(ox_list):
    ox_score_list = []
    
    for ox in ox_list:
        cnt = 0
        score = 0
        
        for i in ox:
            if i == 'X':
                cnt = 0
            if i == 'O':
                cnt+=1
                score+=cnt
        ox_score_list.append(score)
        
    return ox_score_list

N = input()
ox_list = []
for _ in range(int(N)):
    M = input()
    ox_list.append(M)

ox_score_list = ox_print(ox_list)
for i in ox_score_list:
    print(i)



