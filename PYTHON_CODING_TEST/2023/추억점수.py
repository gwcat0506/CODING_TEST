# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    people = {}
    
#     딕셔너리에 추가
    for num in range(len(name)):
        people[name[num]] = yearning[num]

    # 값 계산하기
    ans = []
    for case in photo:
        score = 0
        for name in case:
#             딕셔너리에 있는 경우에만 점수 구하기
            if name in people:
                score += people[name]
        ans.append(score)
    
    return ans