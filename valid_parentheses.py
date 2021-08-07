class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        opening_pair = ['(', '[', '{']
        unclosed_pair = []
        for char in s:
            if char in opening_pair:
                unclosed_pair.append(char)
            else:
                if len(unclosed_pair) > 0:
                    if pairs[unclosed_pair[-1]] == char:
                        unclosed_pair.pop(-1)
                    else:
                        return False
                else:
                    return False
        if len(unclosed_pair) > 0:
            return False
        else:
            return True
        

x = Solution()
print(x.isValid("){"))