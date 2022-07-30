# https://school.programmers.co.kr/learn/courses/30/lessons/68644

# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.



def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = set(answer)
    answer = list(answer)
    return sorted(answer)

# 코드를 너무 길게 짰는데.. 
# sort()-> list만을 위한 메소드, 실행만 시키면 sort()된 상태로 저장
# sorted() ->어떤 객체도 가능 !!, 실행시키면 자동저장XX


from itertools import combinations


# 다른 사람 코드 풀이 
from itertools import combinations

def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer

# combination을 이용한 사람 발견 ! 
# combination을 조합 2로 하여 numbers 리스트 안에서 2개를 뽑도록 한다
# 그리고 뽑은 순열들을 하나씩 들고와서 더해서 append 해준다
# 그리고 집합을 이용하여 중복을 제거하고 list로 type을 다시 변경해준다.
# 그리고 오름차순으로 sort() 해준다.


from itertools import combinations

numbers=[2,1,3,4,1]
ans = []
l = list(combinations(numbers,2))
for i in l:
    ans.append(i[0]+i[1])
ans = set(ans)
ans = list(ans)
print(sorted(ans))
# 