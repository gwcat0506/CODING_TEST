
# 백준
# https://www.acmicpc.net/problem/2775

# k층에 n호에는 몇 명
# 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

# input
# 2
# 1
# 3
# 2
# 3

# 2 
# k n
# 1 3
# 2 3

# output
# 각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

num = int(input())

for i in range(num):
    k = int(input())
    n = int(input())
    
    people = [i for i in range(1,n+1)]
    # print(people)
    for x in range(k):
        for y in range(1,n):
            people[y] += people[y-1]
            
    print(people[-1])