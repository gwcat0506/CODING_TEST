# https://school.programmers.co.kr/learn/courses/30/lessons/12949?language=python3

# 현재 풀이 -> 전치행렬 구성으로 효율적이게 재구성
# arr*을 하면 transpose 가능

def solution(arr1, arr2):
    answer = []
    
    # arr2의 열을 미리 전치 행렬로 변환
    # 1. 배열에 *를 붙이면 됨
    # 2. zip() 함수는 같은 위치의 요소들을 튜플로 묶어 반환
    transposed_arr2 = list(zip(*arr2))
    
    for row in arr1:
        new_row = []
        for col in transposed_arr2:
            new_row.append(sum(a * b for a, b in zip(row, col)))
        answer.append(new_row)
    
    return answer




# 이전 풀이 -> 런타임 에러
def calculate(line_a, current, arr2):
    ans = 0
    for idx in range(len(line_a)):
        ans += line_a[idx]*arr2[idx][current]
    return ans

def solution(arr1, arr2):
    answer = []

    for line_a in arr1 :
        cal_result = []
        for idx in range(len(arr2)):
            cal_result.append(calculate(line_a, idx, arr2))
        answer.append(cal_result)
    
    return answer
