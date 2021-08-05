class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if "" in strs:
            return ""
        else:
            shortest_word = min((word for word in strs if word), key=len)
            prefix = []
            for i in range(len(shortest_word)):
                letter = shortest_word[i]
                for word in strs:
                    if word[i] != letter:
                        return ('').join(prefix)
                prefix.append(letter)     
            return ('').join(prefix)


x = Solution()
print(x.longestCommonPrefix(["dog","doracecar","docar"]))