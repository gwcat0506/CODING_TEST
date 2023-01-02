

N = int(input())

for _ in range(N):
    M = int(input())
    
    case_list = []
    for _ in range(M):
        str_N = input()
        case_list.append(str_N.split(" "))
    
    max_num = 0
    max_school = ''
    for j in range(len(case_list)):
        
        if int(case_list[j][1]) >  max_num:
            max_num = int(case_list[j][1])
            max_school = case_list[j][0]
            
    print(max_school)
            
        
        
        