
def print_complete_num(num_list):
    ans = ''
    for i in range(len(num_list)-1):
        if i == len(num_list)-2:
            ans += str(num_list[i])
        else:
            ans += str(num_list[i])+" + "
        
    return str(num_list[-1])+" = "+ ans

# 약수 구하기 
def complete_num(N):
    num_list = []
    for i in range(1,N+1):
        # 약수구별방법 = 나머지가 0일 때 
        if N%i==0:
            num_list.append(i)
    if sum(num_list[:-1]) == N:
        # 완전수이면
        return print_complete_num(num_list)
    else:
        # 완전수가 아니면
        return str(N)+" is NOT perfect."


num_list2 = []
# 입력받기
while True:
    num = int(input())
    if num == -1:
        break
    else:
        num_list2.append(num)

for j in range(len(num_list2)):
    print(complete_num(num_list2[j]))

