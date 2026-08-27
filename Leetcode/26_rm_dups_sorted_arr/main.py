from v3 import Solution as sol
from icecream import ic 

def main() -> None:
    s = sol()
    # Each test case is: (input_list, expected_k, expected_array)
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
    ]
    
    for nums, expected_k, expected_nums in test_cases:
        # We work on a copy so we don't ruin the original test case definition
        # 1. Call your implementation
        k = s.removeDuplicates(nums, ic) 
        ic(k)
        
        ic(nums)
        t = nums
        ic(t)
        
        # 2. The Judge's logic: Check the returned length
        assert k == expected_k, f"FAILED: Expected k={expected_k}, got {k}"
        
        # 3. The Judge's logic: Check if the first k elements match the expected unique values
        for i in range(k):
            try:
                assert t[i] == expected_nums[i], f"FAILED: At index {i}, expected {expected_nums[i]} but found {t[i]}"
            except AssertionError:
                ic(t, expected_nums)
                break
        else:
            ic("PASSED")
            ic("-" * 25)
            print()
    
if __name__ == "__main__":
    main()
