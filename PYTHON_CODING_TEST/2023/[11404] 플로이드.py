# 1. 2차원 리스트 생성해 모든 값을 무한으로 초기화
# 2. 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
# 3. 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# 4. 점화식에 따라 플로이드 워셜 알고리즘을 수행
# 5. 수행된 결과 출력

import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

# 1. 2차원 리스트 생성해 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 2. 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

# 3. 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    start, end, cost = map(int,input().split())
    graph[start][end] = min(cost,graph[start][end])

# 4. 점화식에 따라 플로이드 워셜 알고리즘을 수행
# k 중간 간선 
# a->k k->b
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
# 5. 수행된 결과 출력

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print('0',end=' ')
        else:
            print(graph[a][b],end=' ')
    print()