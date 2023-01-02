# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3 

def solution(board, moves):
    ans = []
    result = 0
    for move in moves:
        for list_board in board:
            if list_board[move-1] != 0:
#                 0이 아니면 list에 append하고 0으로 초기화
                ans.append(list_board[move-1])
                list_board[move-1] = 0
#          리스트가 2개 이상이면(두 숫자를 비교할 수 있는 상태이면)
                if len(ans)>=2 and ans[-1]==ans[-2]:
                    result+=2
#             리스트에서 끝에서 2개의 원소를 지운다.
                    ans = ans[:-2]
                break
    return result

