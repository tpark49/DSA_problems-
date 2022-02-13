
class TimeMap(object):
    def __init__(self):
        self.dictionary = {}

    def set(self, key, value, timestamp):
        if key not in self.dictionary: 
            self.dictionary[key] = {timestamp:[value]}
        else: 
            if timestamp not in self.dictionary[key]:
                self.dictionary[key][timestamp] = [value]

            else: 
                self.dictionary[key][timestamp].append(value)

    def get(self, key, timestamp):
        if self.dictionary[key]:
            if self.dictionary[key][timestamp]:
                return self.dictionary[key][timestamp]
            else: 
                return self.dictionary[key][max(self.dictionary[key].keys())]
        else: 
            return ""


class TimeMap2(object):
    def __init__(self):
        self.dicitonary = {}
    
    def set(self, key, value, timestamp):
        if key not in self.dicitonary: 
            self.dicitonary[key] = [[timestamp, value]]
        else: 
            self.dicitonary[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dicitonary[key]
        l = 0 
        r = len(arr)-1
        while l <= r: 
            mid = (l+r)//2
            
            if arr[mid][0]>timestamp: 
                r = mid - 1 

            else: 
                l = mid + 1 

        if r <0: 
            return ""
        else: 
            return arr[r][1]
        




if __name__ == "__main__":
    mytime = TimeMap2()
    mytime.set("foo", "bar", 1)
    mytime.set("foo", "bar2", 4)
    print(mytime.get("foo", 5))
