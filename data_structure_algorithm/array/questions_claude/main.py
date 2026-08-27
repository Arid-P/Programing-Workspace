def array_init () -> list:
    n = int(input("Enter the size of the array: "))
    arr = []
    
    for i in range(n):
        value = int(input(f"Enter thevalue of {i+1} element of the array"))
        arr.append(value)
    
    return arr

def one (arr, k, target) -> None:
    from set_one_solution import Solution
    sol = Solution()
    
    outputs = [
        sol.find_second_largest(arr),
        sol.is_palindrome(arr),
        sol.rotate_right(arr, k),
        sol.pair_sum(arr, target),
        sol.two_sum(arr, target)
        ]
    
    return outputs

def one_input () -> None:
    arr = array_init()
    k = input("Enter k: ")
    target = input("Enter target: ")
    
    print("Input completed")
    return one(arr, k, target)

def main() -> None:
    print("Calling input")
    outputs = one_input()
    
    for out in outputs:
        print(out)

if __name__ == '__main__':
    main()