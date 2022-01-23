def lengthOfLongestSubstring(S):
    start = {}
    result = 0 
    s = 0
    for i, c in enumerate(S):
        if c in start and s<=start[c]:
            s = start[c]+1
        else:
            result = max(result, i-s+1)
        
        start[c] = i 

    return result

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))