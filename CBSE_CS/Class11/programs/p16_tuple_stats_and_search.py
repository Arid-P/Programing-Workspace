"""
Program 16: Tuple Operations — Statistics and Linear Search
CBSE Class 11 Practical File

Objective:
1. Input a tuple of numerical values from the user.
2. Manually compute the minimum, maximum, and arithmetic mean of the tuple
   without using built-in min(), max(), or sum().
3. Perform a linear search to find all index positions of a target element in the tuple,
   returning a list of indices, or an empty list if not present.
"""


def compute_tuple_stats(tup: tuple[float, ...]) -> tuple[float, float, float]:
    """
    Compute the minimum, maximum, and mean of a non-empty tuple of numbers manually.

    Parameters:
        tup (tuple[float, ...]): Non-empty tuple of numerical values.

    Returns:
        tuple[float, float, float]: (min_val, max_val, mean_val)

    Raises:
        ValueError: If the tuple is empty.
    """
    if not tup:
        raise ValueError("Empty tuple send as argument.")
    if len(tup) == 1:
        return(*tup, *tup, *tup) #(*tup) * 3
    
    
    stat = [None, None, 0]

    for i in range(len(tup)):
        el: float = tup[i]

        if stat[0] is None or stat[0] > el:
            stat[0] = el
        if stat[1] is None or stat[1] < el:
            stat[1] = el

        stat[2] += el

    return stat[0], stat[1], stat[2]/len(tup)


def tuple_linear_search(tup: tuple[float, ...], target: float) -> list[int]:
    """
    Search for a target value in a tuple and return all index positions where it occurs.

    Parameters:
        tup (tuple[float, ...]): Tuple of elements.
        target (float): Value to find.

    Returns:
        list[int]: List of 0-based indices where target appears (empty list if absent).
    """
    if not tup:
        return []
    if len(tup) == 1:
        return [0] if target == tup[0] else []

    indices: list[int] = []
    for i in range(len(tup)):
        if target == tup[i]:
            indices.append(i)

    return indices


if __name__ == "__main__":
    print("--- Program 16: Tuple Statistics & Linear Search ---")
    raw = input("Enter numbers separated by spaces: ")
    num_list = [float(x) for x in raw.split()]
    data_tuple = tuple(num_list)

    print(f"\nConstructed Tuple: {data_tuple}")
    print(f"Tuple Length:     {len(data_tuple)}")

    if not data_tuple:
        print("Tuple is empty! Cannot compute statistics.")
    else:
        min_v, max_v, mean_v = compute_tuple_stats(data_tuple)
        print(f"\n--- Tuple Statistics ---")
        print(f"Minimum Value: {min_v}")
        print(f"Maximum Value: {max_v}")
        print(f"Mean Value:    {mean_v:.2f}")

        search_val = float(input("\nEnter target number to search: "))
        indices = tuple_linear_search(data_tuple, search_val)

        if indices:
            print(f"Target {search_val} found at index/indices: {indices}")
            print(
                f"Occurrences (verified via tup.count()): {data_tuple.count(search_val)}"
            )
        else:
            print(f"Target {search_val} not found in tuple.")
