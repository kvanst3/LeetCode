class Solution:
    def reverse(self, x: int) -> int:
        if x >= -2^31 & x <=(2^31) -1:
            rev_num = 0
            while x > 0:
                rev_num = (rev_num * 10) + x%10
                x = x//10
