from sqlalchemy import distinct


def lengthOfLongestSubstringKDistinct(s, k):

    distinct = {}
    start = 0 
    maxLen = 0 
    for end in range(len(s)):
        if s[end] in distinct:
            distinct[s[end]]+=1
        else:
            distinct[s[end]] = 1

        while len(distinct)>k:
            distinct[s[start]]-=1
            if distinct[s[start]] == 0: 
                distinct.pop(s[start])
            start+=1

        maxLen = max(maxLen, end-start+1)
    return maxLen


def another2(s, k):
    d = {}
    low, res = 0, 0 
    for i , c in enumerate(s):
        d[c] = i 
        if len(d)>k: 
            low = min(d.values())
            d.pop(s[low])
            low+=1

        res = max(i - low + 1, res)
    return res

if __name__ == "__main__":
    print(lengthOfLongestSubstringKDistinct("aa", 1))
    
