class ListNode:
    def __init__(self, val: int):
        self.val= val
        self.next=None
        
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.head=self.tail=None
        self.len=0
        self.size=k
    def enQueue(self, val: int) -> bool:
        if(self.isFull()):
            return False
        if(self.head is None):
            self.tail=self.head=ListNode(val)
            self.len+=1
            return True
        self.tail.next=ListNode(val)
        self.tail=self.tail.next
        self.len+=1
        return True

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        self.head=self.head.next
        self.len-=1
        return True
        

    def Front(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.head.val

    def Rear(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.tail.val
        
    def isEmpty(self) -> bool:
        return self.len==0

    def isFull(self) -> bool:
        return self.len==self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()