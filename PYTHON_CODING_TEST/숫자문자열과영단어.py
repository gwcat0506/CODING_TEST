# https://school.programmers.co.kr/learn/courses/30/lessons/81301

#  "one4seveneight" -> 1478
#  "23four5six7" -> 234567
#  "1zerotwozero3" -> 10203 
# 로 만드는 문제 

# 보자마자 replace가 떠올랐다 !

def solution(s):
    eng_num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,eng_word in enumerate(eng_num):
        s = s.replace(eng_word,str(i))
        print(s)
    
    return int(s)


# enumerate를 이용해서 i와 eng_word 두 가지 변수를 모두 for문을 한번에 돌릴 수 있었다 ㅎㅎ
# 마지막 return에 int()로 형변환 꼭 해주기 !


# 다른 사람 풀이 
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

# 딕셔너리를 만들어 num_dic.items()를 통해 key와 value를 두 가지를 들고오면서 문제풀기
