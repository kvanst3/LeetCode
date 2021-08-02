class Solution:
    def reverse(self, x: int) -> int:
        pos = True if x > 0 else False
        rev_num = 0
        x = abs(x)
        while x > 0:
            rev_num = (rev_num * 10) + x%10
            x = x//10
        if rev_num >= -2**31 & rev_num <=(2**31) -1:
            return rev_num if pos else rev_num * -1
        else:
            return 0


x = Solution()
print(x.reverse(x=-321))