from typing import List


class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, nums.index(complement)]
            hashmap[nums[i]] = nums[i]