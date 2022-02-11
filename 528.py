import random
class Solution(object):
    def __init__(self, w):
        for i in range(1, len(w)):
            w[i] = w[i] + w[i-1]
        self.w = w 

    def pickIndex(self):
        l = 0 
        r = len(self.w)-1
        rand_int = random.randint(1, self.w[-1])
        while l<=r: 
            mid = (l+r)//2
            
            if self.w[mid] >= rand_int: 
                r = mid - 1
            else: 
                l = mid + 1 

        return l 


if __name__ == "__main__":
    solution = Solution([1,3])
    print(solution.pickIndex())