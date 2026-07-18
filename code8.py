import math
import cmath
import statistics

class AdvancedCalculator:
    def __init__(self):
        """Initializes the Advanced Calculator."""
        print("Advanced Calculator Initialized.")

    # --- Basic Arithmetic ---
    def add(self, *args):
        return sum(args)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return a / b

    # --- Powers and Roots ---
    def power(self, base, exponent):
        """Calculates base raised to the power of exponent."""
        return math.pow(base, exponent)

    def square_root(self, num):
        """Calculates the square root, supporting negative numbers (complex result)."""
        if num < 0:
            return cmath.sqrt(num)
        return math.sqrt(num)

    def nth_root(self, num, n):
        """Calculates the nth root of a number."""
        return num ** (1/n)

    # --- Logarithms ---
    def log(self, num, base=math.e):
        """Calculates logarithm of num to the given base (default is natural log 'e')."""
        if num <= 0:
            raise ValueError("Error: Logarithm domain error (num must be > 0).")
        return math.log(num, base)

    def log10(self, num):
        """Calculates base-10 logarithm."""
        return math.log10(num)

    # --- Trigonometry (Input in degrees) ---
    def _deg_to_rad(self, degrees):
        return math.radians(degrees)

    def sin(self, degrees):
        return math.sin(self._deg_to_rad(degrees))

    def cos(self, degrees):
        return math.cos(self._deg_to_rad(degrees))

    def tan(self, degrees):
        # Handle asymptotes (90, 270, etc.)
        if degrees % 180 == 90:
            raise ValueError("Error: Tangent is undefined at this angle.")
        return math.tan(self._deg_to_rad(degrees))

    # --- Statistics & Combinatorics ---
    def factorial(self, n):
        """Calculates the factorial of an integer."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Error: Factorial requires a non-negative integer.")
        return math.factorial(n)

    def combinations(self, n, k):
        """Calculates nCr (combinations)."""
        return math.comb(n, k)

    def mean(self, *args):
        """Calculates the average of a dataset."""
        return statistics.mean(args)

    def standard_deviation(self, *args):
        """Calculates the standard deviation of a dataset."""
        if len(args) < 2:
            raise ValueError("Error: Standard deviation requires at least 2 data points.")
        return statistics.stdev(args)


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    calc = AdvancedCalculator()

    print("\n--- Testing Advanced Calculator ---")
    
    # Algebra
    print(f"Power (2^10): {calc.power(2, 10)}")
    print(f"Square Root of -16 (Complex Math): {calc.square_root(-16)}")
    print(f"Cube Root of 27: {calc.nth_root(27, 3)}")
    
    # Logarithms
    print(f"Natural Log of 10 (ln 10): {calc.log(10):.4f}")
    print(f"Log base 2 of 256: {calc.log(256, 2)}")
    
    # Trigonometry
    print(f"Sine of 30 degrees: {calc.sin(30):.4f}")
    print(f"Cosine of 60 degrees: {calc.cos(60):.4f}")
    
    # Statistics and Probability
    print(f"Factorial of 6 (6!): {calc.factorial(6)}")
    print(f"Combinations (52 choose 5): {calc.combinations(52, 5)}")
    print(f"Standard Deviation of [10, 12, 23, 23, 16, 23, 21, 16]: {calc.standard_deviation(10, 12, 23, 23, 16, 23, 21, 16):.4f}")