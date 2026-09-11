class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        if len(digits) < 3:
            return 0
            
        # Step 1: Count available digit frequencies
        available = Counter(digits)
        
        # Step 2: Extract unique digits that fit specific position constraints
        hundreds_digits = [d for d in available if d > 0]  # Hundreds cannot be 0
        tens_digits = list(available.keys())
        units_digits = [d for d in available if d % 2 == 0] # Units must be even
        
        count = 0
        
        # Step 3: Direct construction loop
        for h in hundreds_digits:
            available[h] -= 1
            
            for t in tens_digits:
                if available[t] > 0:
                    available[t] -= 1
                    
                    for u in units_digits:
                        if available[u] > 0:
                            count += 1
                            
                    available[t] += 1  # Backtrack tens
                    
            available[h] += 1  # Backtrack hundreds
            
        return count