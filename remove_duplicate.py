class Solution:
    def removeDuplicates(self, nums):
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(nums[:x])
    

x = Solution()
print(x.removeDuplicates([1,1,1,2,2,3,4,5,5,5,6,6,7,9]))