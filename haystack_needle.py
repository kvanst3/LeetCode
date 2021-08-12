class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle:
            return haystack.find(needle)
        return 0

    def strHash(self, haystack, needle):
        n, h = len(needle), len(haystack)
        hash_n = hash(needle)
        for i in range(h-n+1):
            if hash(haystack[i:i+n]) == hash_n:
                return i
        return -1


x = Solution()
print(x.strHash('hello', 'll'))