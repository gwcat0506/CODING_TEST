
# 음의 사이클을 check하는 문제 
 
import sys
INF = 10001
input = sys.stdin.readline

def Bellman(start):
    graph  = [INF]*(N+1)
    graph[start]=0
    
    for i in range(N):
        for start_node,end_node,weight in edge:
            if graph[end_node] > graph[start_node] + weight:
                
                if i==N-1:
                    return True
                graph[end_node] = graph[start_node]+weight
    return False
    
    
TC = int(input())
for _ in range(TC):

    N,M,W = map(int,input().split())
    
    edge = []
    
    # 도로정보
    for _ in range(M):
        start, end, weight = map(int,input().split())
        
        edge.append((start,end,weight))
        edge.append((end,start,weight))

    # 웜홀정보
    for _ in range(W):
        start, end, weight = map(int,input().split())
    
        edge.append((start,end,-weight))
        

    ans = Bellman(1)

    if ans:
        print("YES")
    else:
        print("NO")
    
    
    