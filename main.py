from math import degrees, acos, asin, atan, sin, cos, tan, sqrt

help_message = """
This program takes in triangle lengths and returns the angles

Things you can input for the side lengths:
 - constants, e.g. "123"
 - mathematical expressions using basic arithmetic, e.g. "1 + 2/3"
 - expressions using the following functions:
     acos, asin, atan, sin, cos, tan, sqrt
     using parentheses to wrap the function argument, e.g. "sqrt(2)"

Note: The validity of the triangle is checked before the angles are calculated

"""


def main():
    print(help_message)
    [a, b, c] = take_input()
    if not triangle_valid(a, b, c):
        print("Invalid triangle")
        exit(1)

    # Shift side lengths around in order to calculate all 3 angles
    A = calculate_A(a, b, c)
    B = calculate_A(b, c, a)
    C = calculate_A(c, a, b)

    # Output the angles to 9 decimal places
    # avoids any wacky floating point stuff but still provides decent precision
    print(f"\nAngle A: {round(A, 9)}")
    print(f"Angle B: {round(B, 9)}")
    print(f"Angle C: {round(C, 9)}")


def calculate_A(a, b, c):
    """
    Uses cosine rule to calculate the angle opposite `a`
    """
    return degrees(acos((b * b + c * c - a * a) / (2 * b * c)))


def triangle_valid(a, b, c):
    """
    Uses the triangle validity theorem to weed out invalid triangles
    and prevent errors from occurring while calculating the angles
    """
    return a + b > c and a + c > b and b + c > a


def take_input():
    """
    Takes 3 inputs, evaluates them, converts to floats
    and outputs them in an array
    """
    a = float(eval(input("Input length of side a: ")))
    b = float(eval(input("Input length of side b: ")))
    c = float(eval(input("Input length of side c: ")))

    return [a, b, c]


if __name__ == "__main__":
    main()
