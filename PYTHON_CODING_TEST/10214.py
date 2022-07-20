

N = int(input())

for _ in range(N):
    
    Y_score = 0
    K_score = 0
    for i in range(9):
        M = input()
        Y, K = M.split(" ")
        
        Y_score+=int(Y)
        K_score+=int(K)
        
    if Y_score > K_score:
        print("Yonsei")
    elif Y_score < K_score:
        print("Korea")
    else:
        print("Draw")
