from typing import List
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = [num for num in nums]
        nums_sorted.sort()
        
        left: int = 0
        right: int = len(nums_sorted)-1
        while left < right:
            num_sum = nums_sorted[left] + nums_sorted[right]
            
            if num_sum == target:
                break
            elif num_sum > target:
                right -= 1
            else:
                left += 1
        
        result = []
        for idx, num in enumerate(nums):
            if num == nums_sorted[left]:
                result.append(idx)
                nums[idx] = ''
                break
        
        for idx, num in enumerate(nums):
            if num == nums_sorted[right] :
                result.append(idx)
                break
        
        return result if result[0] < result[1] else result[::-1]

def main():
    sol = Solution()
    num_lists_targets: list[list[int]] = [
        ([2,7,11,15], 9),
        ([3,2,4], 6),
        ([4, 4, 6, 3, 6, 3, 1, 3], 6)
    ]

    for num_list, target in num_lists_targets :
        print(f'for {num_list=} and {target=}', flush=True)
        result: list[int] = sol.twoSum(num_list, target)
        print(f'{result=}\n')
        print('   ')

if __name__ == '__main__':
    main()