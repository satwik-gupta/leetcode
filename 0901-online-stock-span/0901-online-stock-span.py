class StockSpanner:

    def __init__(self):
        self.span = [] 
        
    def next(self, price: int) -> int:
        c = 1
        if not self.span:
            self.span.append([price,c])
            return c
        while self.span:
            ele,val = self.span[-1]  
			
            if ele> price:
                self.span.append([price,c])
                return c
            else:
                c+=val
                self.span.pop()	
        self.span.append([price,c])
        return c