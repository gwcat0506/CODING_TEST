# https://school.programmers.co.kr/learn/courses/30/lessons/12919



def solution(seoul):
    for s in range(len(seoul)) :
        if seoul[s]=="Kim" :
            return "김서방은 "+str(s)+"에 있다" 



# 다른사람 풀이

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 문자열이 아니라 리스트에도 리스트이름.index("궁금한값") 을 해주면 인덱스를 반환해준다 !!
# 꿀팁..