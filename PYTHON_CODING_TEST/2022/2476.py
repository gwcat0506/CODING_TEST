

N = int(input())
score=0
for _ in range(N):
    A, B, C = map(int,input().split())
    
    # 숫자 세 개가 모두 같으면
    if A==B and B==C:
        score+=(10000+A*1000)
    elif (A==B and B!=C ) or (A==C and A!=B ) or (C==B and B!=A ):
        score+=(1000+A*1000)
        
        
    
    
    # 덜햇져용