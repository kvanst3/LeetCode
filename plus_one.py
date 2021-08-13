class Solution:
    def plusOne(self, digits):
        strings = [str(digit) for digit in digits]
        a_string = "".join(strings)
        an_integer = int(a_string) + 1
        d = [int(a) for a in str(an_integer)]
        return d

    # One line 
    def plusOneLiner(self, digits):
        return [int(x) for x in  str(int(''.join(map(str,digits)))+1) ]

    def plusOneRecursive(self, digits):
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            return self.plusOneFaster(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits

    def plusOneFastest(self, digits):
        rev = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            val = rev[i] + carry
            rev[i] = val % 10
            carry = val // 10
        if carry:
            rev.append(1)
        return rev[::-1]

x = Solution()
print(x.plusOneFastest([1,9,9]))