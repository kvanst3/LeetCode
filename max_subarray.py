class Solution:
    def maxSubArray(self, nums):
        dp_table = [0]*len(nums)
        for i, num in enumerate(nums):
            dp_table[i] = max(dp_table[i-1] + num, num)
        return max(dp_table)

    def maxProfit(self, nums):
        cur_max = glo_max = nums[0]
        for num in nums[1:]:
            cur_max = max(num, cur_max + num)
            glo_max = max(cur_max, glo_max)
        return glo_max

x = Solution()
print(x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(x.maxProfit([-2,1,-3,4,-1,2,1,-5,4]))