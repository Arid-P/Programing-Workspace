"""
Program 06: List Operations — Linear Search and Manual Min/Max/Mean
CBSE Class 11 Practical File

Objective:
1. Implement a manual linear search to find a target value in a list (returning its index, or -1 if not found)
   without using the built-in index() or find() methods.
2. Manually compute and return the minimum, maximum, and arithmetic mean of a list of numbers
   without using built-in min(), max(), or sum() functions.
"""

def linear_search(lst: list, target) -> int:
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    
    return -1


def compute_min_max_mean(nums: list[float]) -> tuple[float, float, float]:
    result = [nums[0], nums[0], 0]

    for el in nums:
        #Sum
        result[2] += el

        #min check
        if result[0] > el:
            result[0] = el
        
        #max check
        if result[1] < el:
            result[1] = el   

    return result[0], result[1], result[2]/len(nums)


if __name__ == "__main__":
    raw_input = input("Enter numbers separated by spaces: ")
    data = [float(x) for x in raw_input.split()]
    
    if not data:
        print("List is empty!")
    else:
        # 1. Min, Max, Mean
        minimum, maximum, mean = compute_min_max_mean(data)
        print(f"\n--- Statistics ---")
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Mean:    {mean:.2f}")
        
        # 2. Linear Search
        search_target = float(input("\nEnter a number to search for: "))
        found_idx = linear_search(data, search_target)
        if found_idx != -1:
            print(f"Number {search_target} found at index {found_idx}.")
        else:
            print(f"Number {search_target} was not found in the list.")

