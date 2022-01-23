def longestPalindrome(s): 
    
    result = ""
    for i, c in enumerate(s):

        #odd length
        l, r= i, i 
        while l>=0 and r<len(s) and s[l] == s[r]:
            if len(s[l:r+1])>len(result):
                result = s[l:r+1]
            l-=1
            r+=1
        
        #even length 
        l, r = i, i+1 
        while l>=0 and r<len(s) and s[l] == s[r]:
            if len(s[l:r+1])>len(result):
                result = s[l:r+1]
            l-=1
            r+=1
        
    return result


if __name__ == "__main__":
    print(longestPalindrome("a"))

