
def two_num_sum_target (nums: list[int], target: int) -> list[int] :
    hashmap: dict[int, int] = {}
    
    for idx, num in enumerate(nums[1 : ]) :
        hashmap[num] = idx + 1
    
    print(hashmap)
    for idx, num in enumerate(nums) :
        complement = target - num 
        if complement in hashmap:
            return [idx, hashmap[complement]]
    
    return "Does not exist"


def main () -> None :
    nums: list[int] = [ int(num_str) for num_str in list( input("Enter the list: ").strip().split(',') ) ]
    target: int = int(input("Enter the target number: "))
    
    print(f"The index are: {two_num_sum_target(nums, target)}")
    
    return

if __name__ == "__main__" :
    main()