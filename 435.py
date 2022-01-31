def eraseOverlapIntervals(intervals):

    res = 0 
    intervals.sort()

    prevEnd = intervals[0][1]

    for start, end in intervals[1:]:

        if prevEnd <= start: 
            prevEnd = end 
        else: 
            prevEnd = min(prevEnd, end)

    return res
    

    


if __name__ == "__main__":
    print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))