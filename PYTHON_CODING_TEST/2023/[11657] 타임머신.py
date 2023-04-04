import sys

INF = sys.maxsize
input = sys.stdin.readline

n,m = map(int,input().split())
edge = []
graph = [INF for _ in range(n+1)]

for _ in range(m):
    start,end,weight = map(int,input().split())
    edge.append((start,end,weight))
    

def Bellman_Ford(start):
    
    graph[start]=0
    for i in range(n):
        for start_node,end_node,weight in edge:
            
            if graph[start_node]!=INF and graph[end_node] > graph[start_node]+weight:
                
                # 음의 사이클 존재 check
                if i == n-1:
                    return -1
                graph[end_node] = graph[start_node] + weight        
    return graph
    
    
ans = Bellman_Ford(1)

if ans == -1:
    print(-1)

else:
    for i in range(2,n+1):
        if ans[i]==INF:
            print(-1)
        else:
            print(ans[i])
    # print(graph)
    