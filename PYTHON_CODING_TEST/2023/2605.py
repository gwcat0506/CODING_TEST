# https://www.acmicpc.net/problem/2605
# 줄 세우기 

# insert함수를 통해서 list의 특정 인덱스 부분에 요소를 삽입할 수 있다.
import sys

N = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(N):
    # 뽑은 번호를 기반하여 줄을 세운다.
    result.insert(i-students[i],i+1)

print(*result)
# 정답 출력 end=' '을 통해 붙여서 출력
# for k in result:
#     print(k,end=' ')


# ex) students=[0, 1, 1, 3, 2]
# i=0) ans.insert(0,1) → ans=[1]
# i=1) ans.insert(0,2) → ans=[2,1]
# i=2) ans.insert(1,3) → ans=[2,3,1]
# i=3) ans.insert(0,4) → ans=[4,2,3,1]
# i=4) ans.insert(2,5) → ans=[4,2,5,3,1]
