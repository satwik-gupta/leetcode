class TimeMap:

    def __init__(self):
        self.hm={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.hm):
            self.hm[key]= [(timestamp,value)]
        else:
            self.hm[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.hm or timestamp<self.hm[key][0][0]):
            return ""
        return self.search(self.hm[key],timestamp)
    def search(self, arr, time): 
        left, right = 0,len(arr)-1
        while left<=right:
            middle = left+(right-left)//2
            element = arr[middle][0]
            if element>time:
                right = middle-1
            elif element<time:
                left = middle+1
            else:
                return arr[middle][1]
        return arr[left-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)