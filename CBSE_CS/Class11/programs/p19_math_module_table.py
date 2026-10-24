"""
Program 19: Math Module Applications — Mathematical & Trigonometric Tables
CBSE Class 11 Practical File

Objective:
1. Use Python's built-in `math` module to compute basic mathematical functions:
   - Square root (math.sqrt)
   - Floor and Ceiling (math.floor, math.ceil)
   - Absolute value (math.fabs)
   - Power (math.pow)
2. Generate trigonometric values (sin, cos, tan) by converting degree angles to radians (math.radians).
"""

import math


def compute_math_properties(val: float) -> dict[str, float | None]:
    """
    Compute mathematical properties for a real number using the `math` module.

    Parameters:
        val (float): Input real number.

    Returns:
        dict[str, float | None]: A dictionary with keys:
            - "val": Original value
            - "square": val ** 2
            - "sqrt": math.sqrt(val) if val >= 0 else None (to avoid domain error)
            - "floor": float(math.floor(val))
            - "ceil": float(math.ceil(val))
            - "fabs": math.fabs(val)
    """
    return {
        "val": val,
        "square": val**2,
        "sqrt": math.sqrt(val) if val >= 0 else None,
        "floor": float(math.floor(val)),
        "ceil": float(math.ceil(val)),
        "fabs": math.fabs(val),
    }


def compute_trig_values(angle_degrees: float) -> dict[str, float]:
    """
    Compute trigonometric values for an angle given in degrees.

    Parameters:
        angle_degrees (float): Angle in degrees.

    Returns:
        dict[str, float]: A dictionary with keys:
            - "degrees": Original angle in degrees
            - "radians": math.radians(angle_degrees)
            - "sin": math.sin(radians)
            - "cos": math.cos(radians)
            - "tan": math.tan(radians)
    """
    radians = math.radians(angle_degrees)

    return {
        "degrees": angle_degrees,
        "radians": math.radians(angle_degrees),
        "sin": math.sin(radians),
        "cos": math.cos(radians),
        "tan": math.tan(radians),
    }


if __name__ == "__main__":
    print("--- Program 19: Math Module Applications ---")
    print("1. Mathematical Functions Table")
    print("2. Trigonometric Values Table")
    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        raw = input("\nEnter numbers separated by spaces (e.g. -3.7 0 4 9.5): ")
        numbers = [float(x) for x in raw.split()]

        print("\n" + "=" * 65)
        print(
            f"{'Value':<10} {'Square':<12} {'Sqrt':<12} {'Floor':<10} {'Ceil':<10} {'Fabs':<10}"
        )
        print("=" * 65)
        for num in numbers:
            props = compute_math_properties(num)
            sqrt_str = (
                f"{props['sqrt']:.4f}" if props["sqrt"] is not None else "DomainErr"
            )
            print(
                f"{props['val']:<10.2f} "
                f"{props['square']:<12.2f} "
                f"{sqrt_str:<12} "
                f"{props['floor']:<10.0f} "
                f"{props['ceil']:<10.0f} "
                f"{props['fabs']:<10.2f}"
            )
        print("=" * 65)

    elif choice == "2":
        standard_angles = [0.0, 30.0, 45.0, 60.0, 90.0, 180.0]
        print(f"\nComputing for standard angles: {standard_angles}")

        print("\n" + "=" * 55)
        print(
            f"{'Degrees':<10} {'Radians':<12} {'sin(x)':<12} {'cos(x)':<12} {'tan(x)':<12}"
        )
        print("=" * 55)
        for ang in standard_angles:
            trig = compute_trig_values(ang)
            tan_val = trig["tan"]
            tan_str = f"{tan_val:.4f}" if abs(tan_val) < 1e10 else "Undefined"
            print(
                f"{trig['degrees']:<10.1f} "
                f"{trig['radians']:<12.4f} "
                f"{trig['sin']:<12.4f} "
                f"{trig['cos']:<12.4f} "
                f"{tan_str:<12}"
            )
        print("=" * 55)
    else:
        print("Invalid choice.")
