def lengthOfLongestSubstringTwoDistinct(s):

    distinct = {}

    start = 0
    maxLen = 0 

    for end in range(len(s)): 

        if s[end] in distinct: 
            distinct[s[end]]+=1
        else:
            distinct[s[end]] = 1

        while len(distinct)>2:
            distinct[s[start]] -=1
            if distinct[s[start]] == 0: 
                distinct.pop(s[start])
            start +=1
        
        maxLen = max(maxLen, end - start + 1)

    return maxLen


if __name__ == "__main__":
    print(lengthOfLongestSubstringTwoDistinct("ccaabbb"))


