# https://www.acmicpc.net/problem/2193
# 이친수

# DP


import sys

N = int(sys.stdin.readline())

def fib(N):
    
    A = [0]*100
    A[0]=1
    A[1]=1
    
    if N<=2:
        return 1
    else:
        for x in range(2,N):
            A[x] = A[x-1] + A[x-2]
        
        return A[N-1]
print(fib(N))

# 아래처럼도 풀 수 있다.(참고)
# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-2193%EB%B2%88-%EC%9D%B4%EC%B9%9C%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
    
# 1,2 ->1
# 3 -> 2
# 4 -> 3
# 5 -> 8



# 1자리 부터 이친수를 계속 구해보니
# 이친수의 개수가 피보나치 수열과 일치 한다는 것을 알 수 있었다.


# 1
# 1  1

# 2
# 10    1

# 3
# 101    2
# 100

# 4
# 1010    3
# 1001
# 1000

# 5
# 10100     5
# 10101

# 10010

# 10001
# 10000    8          

# 6
# 101001
# 101000

# 101010

# 100100
# 100101

# 100010
# 100000
# 100001






