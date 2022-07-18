
str_N = input()
num1, num2, num3 = str_N.split(" ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 == num2 and num2 == num3:
    # 숫자 세 개가 모두 같으면
    print(10000+num1*1000)
elif num1 == num2 and num2 != num3 :
    # 숫자 세 개 중 두 개가 같으면
    print(1000+num1*100)
elif num1 == num3 and num1 != num2:
    print(1000+num1*100)
elif num2 == num3 and num2 != num1:
    print(1000+num2*100)
else:
    # 숫자 세 개 모두 다르면 
    print(max(num1, num2, num3)*100)
    
    
    