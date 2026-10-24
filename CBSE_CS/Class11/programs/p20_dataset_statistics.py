"""
Program 20: Comprehensive Dataset Statistics — Manual vs Statistics Module
CBSE Class 11 Practical File

Objective:
1. Manually compute the three central tendencies for a dataset of numbers:
   - Mean (arithmetic average)
   - Median (middle value of sorted list, or average of two middle values)
   - Mode (most frequent value, returning the first-occurring mode in case of ties)
2. Compare manual outputs with Python's standard `statistics` module:
   - `statistics.mean`
   - `statistics.median`
   - `statistics.mode`
"""

from statistics import mean, median, mode


def count_frequencies_dict(lst: list) -> dict[int, int]:
    freq = {}
    for el in lst:
        freq[el] = freq.get(el, 0) + 1
    return freq


def compute_manual_statistics(data: list[float]) -> dict[str, float]:
    """
    Manually compute mean, median, and mode for a non-empty list of numbers.

    Parameters:
        data (list[float]): Non-empty list of numerical values.

    Returns:
        dict[str, float]: A dictionary containing:
            - "mean": Arithmetic mean
            - "median": Median value
            - "mode": Most frequent value (first encountered if tied)

    Raises:
        ValueError: If data is empty.
    """
    if not data:
        raise ValueError("No dataset provide")

    stats = {
        "mean": sum(data) / len(data),
        "median": None,
        "mode": sorted(
            count_frequencies_dict(data).items(), key=lambda tup: -tup[1]
        )[0][0],
    }

    data = sorted(data)
    n = len(data)

    if n % 2 == 1:
        stats["median"] = data[n // 2]  # zero based indexing
    else:
        stats["median"] = (data[n // 2 - 1] + data[n // 2]) / 2

    return stats


def compute_module_statistics(data: list[float]) -> dict[str, float]:
    """
    Compute mean, median, and mode using Python's built-in `statistics` module.

    Parameters:
        data (list[float]): Non-empty list of numerical values.

    Returns:
        dict[str, float]: A dictionary containing:
            - "mean": statistics.mean(data)
            - "median": statistics.median(data)
            - "mode": statistics.mode(data)

    Raises:
        ValueError: If data is empty.
    """
    if not data:
        raise ValueError("No dataset provide")

    return {"mean": mean(data), "median": median(data), "mode": mode(data)}


if __name__ == "__main__":
    print("--- Program 20: Dataset Statistics (Manual vs Module) ---")
    raw = input("Enter numbers separated by spaces (e.g. 10 20 20 30 40 40): ")
    numbers = [float(x) for x in raw.split()]

    if not numbers:
        print("Dataset is empty! Cannot compute statistics.")
    else:
        print(f"\nDataset: {numbers}")
        print(f"Sample Size (N): {len(numbers)}")

        manual_stats = compute_manual_statistics(numbers)
        module_stats = compute_module_statistics(numbers)

        print("\n" + "=" * 55)
        print(f"{'Statistic':<15} {'Manual Method':<18} {'Statistics Module':<18}")
        print("=" * 55)
        print(
            f"{'Mean':<15} {manual_stats['mean']:<18.4f} {module_stats['mean']:<18.4f}"
        )
        print(
            f"{'Median':<15} {manual_stats['median']:<18.4f} {module_stats['median']:<18.4f}"
        )
        print(
            f"{'Mode':<15} {manual_stats['mode']:<18.4f} {module_stats['mode']:<18.4f}"
        )
        print("=" * 55)

        # Verification check
        match_mean = abs(manual_stats["mean"] - module_stats["mean"]) < 1e-9
        match_median = abs(manual_stats["median"] - module_stats["median"]) < 1e-9
        match_mode = abs(manual_stats["mode"] - module_stats["mode"]) < 1e-9

        if match_mean and match_median and match_mode:
            print(
                "\nResult Verification: All manual metrics match the statistics module perfectly!"
            )
        else:
            print(
                "\nResult Verification: Discrepancy detected between manual and module calculations."
            )
