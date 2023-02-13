
import sys
input = sys.stdin.readline

def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1:
        print(from_pos,to_pos)
    else:
        hanoi(n-1,from_pos,aux_pos,to_pos)
        print(from_pos,to_pos)
        hanoi(n-1,aux_pos,to_pos,from_pos)
    return 1

# def hanoi_cnt(k): -> 하노이 탑의 이동 횟수는 2**n-1과 같다.
#     for num in range(k):
#         h_cnt[num+2] = h_cnt[num]+h_cnt[num+1]+num+1
#     return h_cnt[k+1]
# h_cnt = [0]*20
# h_cnt.append(1)
# h_cnt.append(1)

k = int(input())
print(2**k-1)

if k <=20:
    hanoi(k,1,3,2)




