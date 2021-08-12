class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle:
            return haystack.find(needle)
        return 0

x = Solution()
print(x.strStr('hello', 'll'))