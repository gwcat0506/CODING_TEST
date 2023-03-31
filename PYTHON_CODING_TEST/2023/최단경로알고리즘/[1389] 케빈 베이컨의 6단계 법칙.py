
import sys

INF = sys.maxsize
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신 가중치 0으로 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

# 입력받기
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
    

# 플로이드 워샬
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            
print(graph)

