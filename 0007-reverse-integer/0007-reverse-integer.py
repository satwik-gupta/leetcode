class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        limit=2**31
        if (int(x)<0) :
          x = int(x[0]+x[1:][::-1])
        else:
          x =int(x[::-1])
        if -limit <= x <limit:
            return x
        else:
            return 0 