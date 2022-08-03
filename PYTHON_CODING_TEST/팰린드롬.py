
def palindrome(s):
    
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            return(-1)
    
    return 1


print(palindrome('aksdf'))