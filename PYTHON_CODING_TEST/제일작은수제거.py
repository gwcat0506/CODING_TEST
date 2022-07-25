# https://school.programmers.co.kr/learn/courses/30/lessons/12935



def solution(arr):
    if len(arr)==1:
        return [-1]
    else:
        del arr[arr.index(min(arr))]
    
    return arr

# del 명령어 쓰는법
del list이름["값"]
# 하면 값에 해당하는 list요소가 삭제된다.

# 리스트에서 어떤 특정 값의 인덱스를 알고 싶을 때 -> index 이용!!

list이름.index("궁금한 값")