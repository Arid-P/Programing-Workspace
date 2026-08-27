#When array is required

class Solution:
    def removeDuplicates(self, nums: list[int], ic) -> int:
        left, right = 0, 1 
        
        while right < len(nums):
            #When all the duplicates of one elements have been removed
            if nums[left] != nums[right]:
                left += 1 
                right += 1 
                continue
            
            #When duplicates exist
            nums.pop(right)
        
        return len(nums)