class Solution:
    def __init__(self):
        self.roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    def romanToInt(self, s: str) -> int:
        l = [char for char in s]
        result = 0
        counter = 0
        while counter < len(l):
            if counter == len(l) -1:
                result += self.roman_dict[l[counter]]
                return result
            elif self.roman_dict[l[counter]] >= self.roman_dict[l[counter+1]]:
                result += self.roman_dict[l[counter]]
            else:
                result += self.roman_dict[l[counter +1]] - self.roman_dict[l[counter]]
                counter +=1
            counter +=1
        return result

x = Solution()
print(x.romanToInt("III"))
