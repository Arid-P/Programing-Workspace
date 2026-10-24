"""
Program 14: Find the Largest and Second Largest in a List
CBSE Class 11 Practical File

Objective:
Given a list of numbers, determine the largest and the second largest (distinct) elements
in a single pass (O(n) time complexity) without using built-in sort() or sorted().

Example:
Input:  [12, 45, 2, 45, 31, 8]
Output: Largest = 45, Second Largest = 31

Input:  [10, 10, 10]
Output: Largest = 10, Second Largest = None (no distinct second largest)
"""


def find_largest_and_second_largest(
    nums: list[float],
) -> tuple[float | None, float | None]:
    """
    Find the largest and strictly second largest distinct number in a list without sorting.

    Parameters:
        nums (list[float]): Input list of numerical values.

    Returns:
        tuple[float | None, float | None]: (largest, second_largest)
        If list has fewer than 2 distinct elements, second_largest is None.
        If list is empty, return (None, None).
    """
    if not nums:
        return None, None
    elif len(nums) == 1:
        return nums[0], None
    elif len(nums) == 2:
        if nums[0] == nums[1]:
            return (nums[0], None)
        
        return (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])

    max_val = None
    sec_max = None

    for el in nums:
        if max_val is None or el > max_val:
            sec_max = max_val
            max_val = el
        elif el != max_val and (sec_max is None or el > sec_max):
            sec_max = el

    return (max_val, sec_max)


if __name__ == "__main__":
    print("--- Program 14: Largest and Second Largest in List ---")
    raw = input("Enter numbers separated by spaces: ")
    numbers = [float(val) for val in raw.split()]

    first, second = find_largest_and_second_largest(numbers)
    print(f"\nGiven list: {numbers}")
    print(f"Largest:        {first}")
    print(f"Second Largest: {second}")
