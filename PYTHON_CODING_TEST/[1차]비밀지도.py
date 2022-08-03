# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    ans = []
    for i in range(len(arr1)): 
        bin_num = bin(arr1[i])[2:]
        if len(bin_num)<n:
            arr1[i] = "0"*(n-len(bin_num))+bin_num
        else:
            arr1[i] = bin_num

        bin_num = bin(arr2[i])[2:]
        if len(bin_num)<n:
            arr2[i] = "0"*(n-len(bin_num))+bin_num
        else:
            arr2[i] = bin_num
    
    for c in range(n):
        l = ''
        for b in range(n):
            if arr1[c][b]=='1' or arr2[c][b]=='1':
                l+="#"
            elif arr1[c][b]=='0' and arr2[c][b]=='0':
                l+=" "
        ans.append(l)
        
    return ans

# bin 함수를 이용하면 이진수를 쉽게 구할 수 있다. 
# bin(숫자)[2:]

# 다른 사람 풀이 
# zip으로 두 가지 리스트를 동시에 for문 돌릴 수 있다 ! 
def solution(n, arr1, arr2):
    fin_list=[]
    for i, j in zip(arr1, arr2):
        list1=int(bin(i)[2:])
        list2=int(bin(j)[2:])
        fin_list.append(str(list1+list2).zfill(n))
    fin=[]
    for a in fin_list:
        fin_r=''
        for b in a:
            if b=='0':
                fin_r+=" "
            else:
                fin_r+="#"
        fin.append(fin_r)
    return fin