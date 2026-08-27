#When number of unique elements is required
class Solution:
    def removeDuplicates(self, nums: list[int], ic) -> int:
        left, right = 0, 1 
        unique_elements = 1
        
        arr_size = len(nums)
        while right < arr_size:
            #When new elements encountered update unique_elements
            if nums[left] != nums[right]:
                unique_elements += 1
            
            left += 1 
            right += 1 
        
        return unique_elements