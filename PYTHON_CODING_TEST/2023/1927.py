# https://www.acmicpc.net/problem/1927
# 최소 힙


# 1. 시간 초과 코드(힙이라는 것을 무시하고 그냥 list로 구현해봄..)

# 연산의 개수
N = int(input())

x_list = []
for _ in range(N):
    x = int(input())
    
    # x가 0이면 가장 작은 값 출력 & 배열에서 제거
    if x !=0:
        x_list.append(x)
    else:
        # 배열이 비어있을 경우 0출력
        if len(x_list)==0:
            print(0)
        else:
            # 가장 작은 값 출력
            print(min(x_list))
            # 배열에서 제거
            del x_list[x_list.index(min(x_list))]


# 2. 힙으로 다시 짰지만 시간 초과
# 파이썬에서는 heapq 모듈을 사용해서 최소 힙과 최대 힙을 구현할 수 있다.
import heapq


N = int(input())
heap = []

# 힙에 Push 
for _ in range(N):
    x = int(input())
    
    # x가 0이 아니면 heap에 push
    if x !=0:
        heapq.heappush(heap, x)
    elif len(heap)==0:
            print(0)
    else:
        # 가장 작은 값 출력 및 제거
        print(heapq.heappop(heap))
            
# heappop(heap)
# heap에서 가장 작은 항목을 pop하고 반환해주는 메소드 
# * 주의 -> 힙이 비어 있을 때 heappop 메소드를 호출하면 IndexError 발생



# 3. 힙 모듈(heapq)와 sys 사용
import heapq
import sys

N = int(sys.stdin.readline())
heap = []

# 힙에 Push 
for _ in range(N):
    x = int(sys.stdin.readline())
    
    # x가 0이 아니면 heap에 push
    if x !=0:
        heapq.heappush(heap, x)
    elif len(heap)==0:
            print(0)
    else:
        # 가장 작은 값 출력 및 제거
        print(heapq.heappop(heap))