# https://school.programmers.co.kr/learn/courses/30/lessons/12901

# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?

def solution(a, b):
    
    day_dict = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    month_dict = [31,29,31,30,31,30,31,31,30,31,30,31]
    day_sum = 0 
    for i in range(a-1):
        day_sum+=month_dict[i]
    
    return day_dict[(day_sum+b)%7-3]

# 다른 풀이(위의 코드 축소해보기)
def solution(a, b):
    
    day_dict = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    month_dict = [31,29,31,30,31,30,31,31,30,31,30,31]

    return day_dict[(sum(month_dict[:a-1])+b)%7-3]



