

n, m = map(int,input().split())
min_max_num = 0
for _ in range(n):
    num_list = list(map(int,input().split()))
    if min_max_num < min(num_list):
        min_max_num = min(num_list)
    
print(min_max_num)
    
# 좀 더 쉽게 구현

result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    # 가장 작은 수 중에서 가장 큰 수 찾기
    result = max(result,min_value)
print(result)