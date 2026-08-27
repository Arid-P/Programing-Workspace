#When array is required,

class Solution:
    def removeDuplicates(self, nums: list[int], ic) -> int:
        unique_elements = 1
        removed_nums = [nums[0]]
        
        for num in nums:
            if num != removed_nums[-1]:
                removed_nums.append(num)
                unique_elements += 1
        
        nums = [el for el in removed_nums]
        ic(removed_nums, unique_elements)
        return unique_elements