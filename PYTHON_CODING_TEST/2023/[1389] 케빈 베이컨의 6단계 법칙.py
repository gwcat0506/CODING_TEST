
import sys

# INF = sys.maxsize
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[n]*(n+1) for _ in range(n+1)]


# 입력받기
for _ in range(m):
    a,b = map(int,input().split())
    # 양방향 주의
    graph[a][b]=1
    graph[b][a]=1

# 플로이드 워샬
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j] = 0
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            
            
# 최댓값으로 초기화 
total = n*6

now =0
for i in range(1, n + 1):
    if sum(graph[i]) < total:
        total = sum(graph[i])
        now = i
        # 각 사람이 가지는 관계 비용이 현재 저장된 값보다 작다면 비용을 갱신해주고
        # 어떤 사람이 인지 표시해줍니다.
print(now)
# 가장 적은 비용