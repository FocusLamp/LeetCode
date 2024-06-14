class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        minIncrement = 0

        nums.sort()


        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] + 1 - nums[i]
                minIncrement += increment


                nums[i] = nums[i - 1] + 1
        
        return minIncrement
