class MyCircularDeque:

    def __init__(self, k: int):
        self.head=k-1
        self.tail=0
        self.len=0
        self.size=k
        self.cdeque=[0]*k

    def insertFront(self, val: int) -> bool:
        if(self.isFull()):
            return False
        self.cdeque[self.head]=val
        self.head=(self.head-1)%self.size
        self.len+=1
        return True
    
    def insertLast(self, val: int) -> bool:
        if(self.isFull()):
            return False
        self.cdeque[self.tail]=val
        self.tail=(self.tail+1)%self.size
        self.len+=1
        return True

    def deleteFront(self) -> bool:
        if(self.isEmpty()):
            return False
        self.head=(self.head+1)%self.size
        self.len-=1
        return True
    def deleteLast(self) -> bool:
        if(self.isEmpty()):
            return False
        self.tail=(self.tail-1)%self.size
        self.len-=1
        return True
    def getFront(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.cdeque[(self.head+1)%self.size]

    def getRear(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.cdeque[(self.tail-1)%self.size]

    def isEmpty(self) -> bool:
        return self.len==0

    def isFull(self) -> bool:
        return self.len==self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()