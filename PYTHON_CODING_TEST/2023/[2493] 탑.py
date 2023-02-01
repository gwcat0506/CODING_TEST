import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))

st = []
# pair로 push 
st.append((0,N_list[0]))

result = [0]

for i in range(1,N):
      
    if st[-1][1] < N_list[i] :
        # 9 < 5
        st.pop() 
        if len(st)==0:
            result.append(0) 
        else:
            # print(st[-1])
            result.append(N_list.index(st[-1][1])+1)
    else:
        # print(st[-1])
        result.append(N_list.index(st[-1][1])+1)
    st.append((i+1,N_list[i]))
    # print(st)
print(*result)
        

# for i in range(1,N):
#     # 입력받은 값이 현재 높이 값 보다 낮으면 pop
#     if st[-1] < N_list[i] :
#         5 < 7
#         st.pop()
#         # pop 후 stack 비어있을 경우 
#         if len(st)==0:
#             idx.append(0)
#         else:
#             idx.append(i)
#     else: 
#         idx.append(i)
        
    
#     st.append(N_list[i])
    
    
# print(*idx)
        

