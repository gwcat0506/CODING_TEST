from posixpath import split


str_N = input()

A, B = str_N.split(" ")

if int(A) > int(B):
    print(">")
elif int(A) < int(B):
    print("<")

else:
    print("==")
    


# split을 쓸때는 A.split("나눠지는 기준")
