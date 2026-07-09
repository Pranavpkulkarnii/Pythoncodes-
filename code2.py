import cmath


def parse_complex(value: str) -> complex:
    """Parse a string into a Python complex number."""
    text = value.strip()
    if not text:
        raise ValueError("Empty input")
    # Allow users to enter j for imaginary values and ^ for exponents.
    text = text.replace("^", "**")
    if text.endswith("j") or "j" in text:
        return complex(text)
    return complex(float(text))


def solve_linear(a: complex, b: complex) -> complex:
    """Solve ax + b = 0 for x."""
    if a == 0:
        raise ValueError("Coefficient a must not be zero for a linear equation.")
    return -b / a


def solve_quadratic(a: complex, b: complex, c: complex) -> tuple[complex, complex]:
    """Solve ax^2 + bx + c = 0 using the quadratic formula."""
    if a == 0:
        raise ValueError("Coefficient a must not be zero for a quadratic equation.")
    discriminant = b * b - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return root1, root2


def format_complex(value: complex) -> str:
    """Format complex numbers cleanly for output."""
    real = f"{value.real:.6g}"
    imag = f"{abs(value.imag):.6g}"
    if value.imag == 0:
        return real
    if value.real == 0:
        return f"{imag}j" if value.imag > 0 else f"-{imag}j"
    sign = "+" if value.imag >= 0 else "-"
    return f"{real}{sign}{imag}j"


def main() -> None:
    print("Complex Equation Solver")
    print("1) Solve linear equation: a*x + b = 0")
    print("2) Solve quadratic equation: a*x^2 + b*x + c = 0")

    choice = input("Choose an option (1 or 2): ").strip()
    if choice == "1":
        a = parse_complex(input("Enter coefficient a (e.g. 1+2j): "))
        b = parse_complex(input("Enter coefficient b (e.g. 3-4j): "))
        solution = solve_linear(a, b)
        print(f"Solution: x = {format_complex(solution)}")
    elif choice == "2":
        a = parse_complex(input("Enter coefficient a (e.g. 1+2j): "))
        b = parse_complex(input("Enter coefficient b (e.g. 3-4j): "))
        c = parse_complex(input("Enter coefficient c (e.g. 5+6j): "))
        root1, root2 = solve_quadratic(a, b, c)
        print(f"Root 1: x = {format_complex(root1)}")
        print(f"Root 2: x = {format_complex(root2)}")
    else:
        print("Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
