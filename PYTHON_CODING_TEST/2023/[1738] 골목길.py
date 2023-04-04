# 아직 덜 품 

import sys
INF = -sys.maxsize
input = sys.stdin.readline

def Bellman(start):
    graph  = [INF]*(N+1)
    path  = [0]*(N+1)
    graph[start]=0
    
    for i in range(N):
        for start_node,end_node,weight in edge:
            if graph[start_node]!=-INF and graph[end_node] < graph[start_node] + weight:
                # path[start_node] = startnode
                if i==N-1:
                    return False
                graph[end_node] = graph[start_node]+weight
    return True
    
    
N,M = map(int,input().split())


edge = []
# 도로정보
for _ in range(M):
    start, end, weight = map(int,input().split())
    edge.append((start,end,weight))
    
ans = Bellman(1)

if ans:
    print("YES")
else:
    print("NO")


