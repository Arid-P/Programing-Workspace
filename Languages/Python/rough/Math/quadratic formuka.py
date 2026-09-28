import math as m


def printing(discriminant, a, b) -> None:
    print(f" -{b} +_ root({discriminant}) / {2*a} ")
    return


def main() -> None:
    # Get input values for the quadratic equation
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    
    # Calculate the discriminant to determine if roots are real
    discriminant = b**2 - 4 * a * c
    
    # Check if roots are real or imaginary
    if discriminant >= 0:
        # Real roots calculation
        x1 = ((-1 * b) + m.sqrt(discriminant)) / (2 * a)
        x2 = ((-1 * b) - m.sqrt(discriminant)) / (2 * a)
        if type(x1) != 'int' :
          printing(a=a, b=b, discriminant=discriminant)
        else :
          print(f"First root: {x1}")
          print(f"Second root: {x2}")
        
    else:
        # Imaginary roots case
        real_part = -b / (2 * a)
        imaginary_part = m.sqrt(-discriminant) / (2 * a)
        print(f"First root: {real_part} + {imaginary_part}i")
        print(f"Second root: {real_part} - {imaginary_part}i")
    
    return

if __name__ == "__main__":
    main()