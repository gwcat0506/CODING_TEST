
# 그리디 알고리즘 

# 5 8 3
# 2 4 5 4 6

N, M, K = map(int,input().split())
N_list = list(map(int,input().split()))

# 내림차순 정렬하기
N_list.sort(reverse=True)

score = 0
cnt=0
a=0

while True:
    if a == M:
        break
    if cnt<K:
        score+=N_list[0]
        cnt+=1
    elif cnt>=K:
        score+=N_list[1]
        cnt=0
    a+=1
print("score",score)


# 다른 풀이
# 가장 큰 수가 더해지는 횟수를 계산
# ex 6 6 6 5 6 6 6 5 
# 큰 수가 더해지는 횟수는 6

count = int(M/(K+1))*K
count+= M%(K+1)

score = 0
score += (count)*N_list[0]
score += (M-count)*N_list[1]

