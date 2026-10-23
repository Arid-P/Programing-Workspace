"""
Program 07: Swap Even and Odd Positioned Elements in a List
CBSE Class 11 Practical File

Objective:
Input a list of elements from the user. Swap adjacent elements at even and odd indices
(i.e., swap index 0 with index 1, index 2 with index 3, etc.) in place.
If the list contains an odd number of elements, the last element remains in its position.
"""


def swap_adjacent_elements(lst: list) -> None:
    if len(lst) <= 1:
        return 

    upper_limit = ((len(lst) // 2) * 2) 
    for i in range(0, upper_limit, 2):  # Runs like 0, 2, 4, 6
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        #we could utilise the old loop conditon by doing 2*i in index


if __name__ == "__main__":
    raw_input = input("Enter list elements separated by spaces: ")
    user_list = raw_input.split()

    print(f"\nOriginal List: {user_list}")
    swap_adjacent_elements(user_list)
    print(f"Swapped List:  {user_list}")
