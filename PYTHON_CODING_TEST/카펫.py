# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 풀어보니 별거 아니다! 쫄지 말자 !
def solution(brown, yellow):
    yellow_num = [1]
    
#     yello 약수 구하기
    for i in range(2,yellow//2+1):
        if yellow%i==0:
            yellow_num.append(i)
    
    for j in yellow_num:
        if j*2+(yellow//j)*2+4 == brown:
            return [max(j+2,yellow//j+2),min(j+2,yellow//j+2)]
    
