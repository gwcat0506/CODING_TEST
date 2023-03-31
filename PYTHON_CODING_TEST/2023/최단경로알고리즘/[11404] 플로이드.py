
import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

# 그래프 생성
graph = [ [INF]*(n+1) for _ in range(n+1) ]

# 자기 자신으로 가는 그래프 초기화 
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0


for _ in range(m):
    start, end, weight = map(int,input().split())
    graph[start][end] = min(graph[start][end],weight)


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            
            
# 정답출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
