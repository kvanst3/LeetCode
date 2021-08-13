class Solution:
    def maxSubArray(self, nums):
        dp_table = [0]*len(nums)
        for i, num in enumerate(nums):
            dp_table[i] = max(dp_table[i-1] + num, num)
        return max(dp_table)



x = Solution()
print(x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))