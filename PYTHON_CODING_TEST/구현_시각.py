
n = int(input())

cnt=0
for n in range(n+1):
    for i in range(60):
        for j in range(60):
            # if (str(n) or str(i) or str(j) ) == '3':
            if '3' in str(n)+str(i)+str(j):
                cnt+=1
print(cnt)