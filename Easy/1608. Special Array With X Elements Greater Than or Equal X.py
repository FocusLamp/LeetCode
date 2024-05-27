class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        index = 0
        previous_number = -1
        greater_than_or_equal = len(nums)

        while index < len(nums):
            if previous_number < nums[index] == greater_than_or_equal or (previous_number < greater_than_or_equal < nums[index]):
                return greater_than_or_equal 
            

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            previous_number = nums[index]
            index += 1
            greater_than_or_equal = len(nums) - index
        
        return -1
