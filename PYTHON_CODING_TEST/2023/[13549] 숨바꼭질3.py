from collections import deque
import sys

input = sys.stdin.readline

MAX = 100001
visited = [False] * MAX
arr = [-1] * MAX

n,k = map(int, input().split())
dq = deque()
dq.append(n)
visited[n] = True
arr[n] = 0

while dq:
    now = dq.popleft()
    if now*2 <= MAX and visited[now*2] == False:  # 순간이동
        # 순간이동은 가중치를 더하지 XX
        dq.appendleft(now*2) 
        visited[now*2] = True
        arr[now*2] = arr[now]
        
    if now + 1 <= MAX and visited[now+1] == False: # x+1 이동
        dq.append(now+1)
        visited[now+1] = True
        arr[now+1] = arr[now] + 1
        
    if now - 1 >= 0 and visited[now-1] == False: # x-1 이동
        dq.append(now-1)
        visited[now-1] = True
        arr[now-1] = arr[now] + 1
        
print(arr[k])