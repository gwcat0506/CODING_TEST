# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    ans = []
    for command in commands:
        i,j,k= command[0],command[1],command[2]
        new_array = array[i-1:j]
        new_array.sort()
        # print(new_array) -> print()하면서 확인하기 꿀팁 !!
        ans.append(new_array[k-1])
    return ans

# 다른 사람 풀이
def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# commands를 그냥 ijk로 바로 받아도 됨 !! 꿀팁
