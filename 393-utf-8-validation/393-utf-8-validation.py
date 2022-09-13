class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def is_continuation(num):
            return num >= 128 and num <= 191
        
        i = 0
        while i < len(data):

            if data[i] <= 127:
                i += 1

            elif data[i] >= 192 and data[i] <= 223:
                try:
                    if not is_continuation(data[i+1]):
                        return False
                except IndexError:
                    return False
                i += 2

            elif data[i] >= 224 and data[i] <= 239:
                try:
                    if not is_continuation(data[i+1]) or not is_continuation(data[i+2]):
                        return False
                except IndexError:
                    return False
                i += 3

            elif data[i] >= 240 and data[i] <= 247:
                try:
                    if not is_continuation(data[i+1]) or not is_continuation(data[i+2]) or not is_continuation(data[i+3]):
                        return False
                except IndexError:
                    return False
                i += 4
            
            else:
                return False
            
        return True