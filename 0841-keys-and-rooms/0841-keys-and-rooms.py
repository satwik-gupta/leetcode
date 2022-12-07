class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        stack=[False]*n
        stack[0]=True
        q=[0]
        while(q):
            x=q.pop(0)
            l=rooms[x]
            for y in l:
                if stack[y]==False:
                    stack[y]=True
                    q.append(y)
        if False in stack:
            return False
        return True