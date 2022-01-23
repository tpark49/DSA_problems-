from calendar import c


def characterReplacement(s, k):

    l = 0 
    result = 0 
    count = {}
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while r-l+1 - max(count.values()) > k: 
            count[s[l]]-=1
            l+=1
        
        result = max(result, r-l+1)
    return result

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print(characterReplacement(s, k))