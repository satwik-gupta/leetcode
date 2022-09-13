class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # check if it is formed 10xxxxxx
        def is_continuation(num):
            return num >= 128 and num <= 191
        
        i = 0
        while i < len(data):
            # 1-byte UTF8 character
            if data[i] <= 127:
                i += 1
                
            # 2-byte UTF8 character
            elif data[i] >= 192 and data[i] <= 223:
                try:
                    if not is_continuation(data[i+1]):
                        return False
                except IndexError: # not sufficient numbers for 2-byte UTF8 code
                    return False
                i += 2
                
            # 3-byte UTF8 character
            elif data[i] >= 224 and data[i] <= 239:
                try:
                    if not is_continuation(data[i+1]) or not is_continuation(data[i+2]):
                        return False
                except IndexError: # not sufficient numbers for 3-byte UTF8 code
                    return False
                i += 3
            
            # 4-byte UTF8 chatacter
            elif data[i] >= 240 and data[i] <= 247:
                try:
                    if not is_continuation(data[i+1]) or not is_continuation(data[i+2]) or not is_continuation(data[i+3]):
                        return False
                except IndexError: # not sufficient numbers for 4-byte UTF8 code
                    return False
                i += 4
            
            else:
                return False
            
        return True