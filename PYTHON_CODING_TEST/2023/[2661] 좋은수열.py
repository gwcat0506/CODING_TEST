# 숫자 1, 2, 3으로만 이루어지는 수열
import sys

n = int(sys.stdin.readline())

def good_seq(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True



def dfs(num):
    # print(num)
    if len(num)==n:
        # 좋은 수열이면 출력
        print(num)
        exit()
    
    for i in '123':
        if good_seq(num+i):
            dfs(num+i)
        

dfs('1')
