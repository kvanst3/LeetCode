class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(digit) for digit in digits]
        a_string = "".join(strings)
        an_integer = int(a_string) + 1
        d = [int(a) for a in str(an_integer)]
        return d


