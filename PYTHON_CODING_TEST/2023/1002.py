

import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    
    # 두 원의 중심 사이 거리 
    dis = math.sqrt((x1-x2)**2+(y1-y2)**2)
    
    if dis ==0: #두 원의 중심이 같으면
        if r1==r2: #그 중에서도 크기도 같은 경우 (겹치는 경우) -> 무한개의 점(-1 출력)
            print(-1)
        else: #원 안에 원이 들어가 있는 경우
            #아예 만나지 않으므로 0 출력
            print(0)
    
    else:
        # 중심사이 거리가 반지름의 합이 같으면 접접은 1개
        # 큰 반지름 - 작은 반지름 -> 중심사이 거리여도 내접하므로 접점은 1개
        if (r1+r2 == dis) or abs(r1-r2)==dis: 
            print(1)
        
        # 원의 중심사이의 거리보다 반지름의 합이 더 크고, 반지름의 차가 더 작으면 접점이 2개 
        elif ((abs(r1-r2) < dis) and (dis < r1+r2)):
            print(2)
        else:
            #그게 아니면 접점은 없음
            print(0)
    
    