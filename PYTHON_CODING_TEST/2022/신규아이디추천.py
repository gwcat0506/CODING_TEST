# https://school.programmers.co.kr/learn/courses/30/lessons/72410




def solution(new_id):
    #     1단계
    new_id=new_id.lower()
    print(new_id)
#     2단계
    ans=''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            ans += word
    new_id = ans
    
    print(new_id)
    
#     3단계
    while True:
        if new_id.find('..')==-1:
            break
        else:
            new_id=new_id.replace('..','.')
    print(new_id)
#     4단계
    if len(new_id)>0: 
        if new_id[0]=='.':
            # if len(new_id)!=1
            new_id = new_id[1:]
    if len(new_id)>0: 
        if new_id[-1]=='.':
            new_id = new_id[:-1]
    # print(new_id)
    # 5단계
    if new_id=='':
        new_id = 'a'
#     6단계
    if len(new_id)>=16:
        new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
#     7단계
    if len(new_id)<=2:
        new_id=new_id+new_id[-1]*(3-len(new_id))
        
    return new_id


# 제일 어려웠던 단계 -> 2단계
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.

# 문자열이 알파벳인지 확인하기 -> isalpha()
# 문자열이 숫자인지 확인하기 -> isdigit()

# 문자열이 알파벳&숫자 인지 확인하기 -> isalnum()

isalpha()를 통해 문자열이 알파벳인지 확인할 수 있다는 것 알아두기 ! 