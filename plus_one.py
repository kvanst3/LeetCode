class Solution:
    def plusOne(self, digits):
        strings = [str(digit) for digit in digits]
        a_string = "".join(strings)
        an_integer = int(a_string) + 1
        d = [int(a) for a in str(an_integer)]
        return d

    def plusOneFaster(self, digits):
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            return self.plusOneFaster(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits

x = Solution()
print(x.plusOneFaster([1,9,9]))