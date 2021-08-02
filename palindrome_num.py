class StrSolution:
    """Solution converting to string"""
    def isPalindrome(self, x: int) -> bool:
        rev_x = str(x)[::-1]
        if rev_x == str(x):
            return True

class IntSolution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            rev_num = 0
            ori_num = x
            while x > 0:
                rev_num = (rev_num * 10) + x%10
                x = x//10
            if rev_num == ori_num:
                return True

x = IntSolution()
print(x.isPalindrome(121))