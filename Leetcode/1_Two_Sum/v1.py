from typing import List
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: list[int] = [0, 1]
        
        while result[0] < len(nums):
            while result[1] < len(nums) :
                num_sum = nums[result[0]] + nums[result[1]]
                if num_sum == target :
                    return result
                result[1] += 1
            result[0] += 1
            result[1] = result[0] + 1
        
   

def main():
    sol = Solution()
    num_lists: list[list[int]] = [
        [2,7,11,15],
        [3,2,4],
        [3,3]
    ]
    
    targets: list[int] = [9, 6, 6]
    
    for i in range(3) :
        num_list = num_lists[i]
        target = targets[i]
        
        result: list[int] = sol.twoSum(num_list, target)
        print(f'for {num_list=} and {target=}\n{result=}\n')
        print('   ')

if __name__ == '__main__':
    main()