
# 45분 일찍 알람 설정하기

str_N = input()
H, M = str_N.split(" ")

H = int(H)
M = int(M)
 
# OO시OO분을 OOO분으로 바꾸기
# ex 12:20 -> 740분
all_minute = H*60+M

minute_minus_45 = all_minute - 45

H = minute_minus_45//60
M = minute_minus_45%60

# H가 음수가 될 경우 
if H < 0:
    H = H+24

print(H, M)


