def find_max_min (nums: list) -> None :
    if len(nums) == 1 :
        print(f'max, min both are {nums[0]}')

    max_num = nums[0]
    min_num = nums[0]

    for num in nums[1:] :
        max_num = max(max_num, num)
        min_num = min(min_num, num)

    print(f'{max_num = },   {min_num = }')

def main () -> None :
    nums: list = [4, 2, 8, 6, 3]
    find_max_min(nums)
    return

if __name__ == "__main__" :
    main()