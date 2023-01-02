
# 모르겠다 

# nxm 맵 생성
n,m = map(int,input().split())

# d = [[0]*m for _ in range(n)]
# d
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0


# 칸의 좌표(a,b)와 바라보는 방향 d(0북쪽 1동쪽 2남쪽 3서쪽)
a,b,d = map(int,input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

print(array)

# 북 동 남 서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]






